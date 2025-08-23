from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import emit, join_room

#Import decision problem classes
from decision_problems import *

# Import the in-memory store of game sessions
from game_sessions import get_game_session, has_game_session, Player, GameSession, GameSessionStatus         


def register_socket_handlers(socketio):
    
    # Socket for game master joining the room
    @socketio.on('join_as_master')
    def join_as_master(data):
        try:
            game_session_id = data['game_session_id']
            join_room(game_session_id)
            print(f"Game Master joined room {game_session_id}")
        except Exception as e:
            emit('error', 
                 {'message': f'Unexpected error occured: {e}'},
                 to=request.sid, # Only send to the related user
                 )

    
    # Socket for requesting the leader board data
    @socketio.on('get_leaderboard')
    def get_leaderboard(data):
        try:
            game_session: GameSession = get_game_session(data['game_session_id'])
            leaderboard = game_session.get_leaderboard()
            emit('leaderboard_data', {'leaderboard': leaderboard})
        except Exception as e:
            emit('error', 
                {'message': f'Unexpected error occured: {e}'},
                to=request.sid, # Only send to the related user
                )


    # Socket for the game master to start the game
    @socketio.on('start_game')
    def on_start(data):
        try:
            game_session: GameSession = get_game_session(data['game_session_id'])
            game_session.start()
            emit('game_started', room=game_session.id)
        except Exception as e:
            emit('error', 
                {'message': f'Unexpected error occured: {e}'},
                to=request.sid, # Only send to the related user
                )


    # Socket for the game master to end the game
    @socketio.on('end_game')
    def on_end(data):
        try:
            game_session: GameSession = get_game_session(data['game_session_id'])
            game_session.end()
            emit('game_ended', room=game_session.id)
        except Exception as e:
            emit('error', 
                {'message': f'Unexpected error occured: {e}'},
                to=request.sid, # Only send to the related user
                )


    # Sockets for player joining the room
    @socketio.on('join_game')
    def on_join(data):
        try:
            try:
                game_session: GameSession = get_game_session(data['game_session_id'])
            except:
                emit('error', {'message': '⛔ Invalid Game ID'}) 
                return
        
            username = data['username']

            if game_session.status == GameSessionStatus.STARTED:
                emit('error', {'message': f'⛔ Game has already started'})
                return
            
            if game_session.status == GameSessionStatus.ENDED:
                emit('error', {'message': f'⛔ Game has already ended'})
                return
                
            if username in game_session.players:
                emit('error', {'message': f'⛔ User name already taken'}) 
            else:
                join_room(game_session.id)
                game_session.add_player(username)
                print(f'emit player_joined: {username} joined game {game_session.id}')
                emit('player_joined', 
                    {'username': username},
                    room=game_session.id)
        except Exception as e:
            emit('error', 
                {'message': f'Unexpected error occured: {e}'},
                to=request.sid, # Only send to the related user
                )


    # Socket for the player to get the level data
    @socketio.on('get_level_data')
    def handle_get_level_data(data):
        try:
            print(f"handle get_level_data {data}")

            if not has_game_session(data['game_session_id']):
                emit('level_data', 
                     {'new_game': True},
                     to=request.sid, # Only send to the user that has requested the data
                    )
                return

            game_session: GameSession = get_game_session(data['game_session_id'])

            if not game_session.has_player(data["username"]):
                emit('level_data', 
                     {'new_game': True},
                     to=request.sid, # Only send to the user that has requested the data
                    )
                return

            player: Player = game_session.get_player(data["username"])
            decision_problem: DecisionProblem = game_session.decision_problem

            # Check if player is done
            if player.current_level == decision_problem.nr_levels:
                emit('level_data', 
                     {'progress': player.progress},
                     to=request.sid, # Only send to the user that has requested the data
                    )
                return
            
            # Check if player is requesting a different level than the current level
            level_idx = data.get('level_idx', player.current_level)
            level: DecisionProblemLevel = decision_problem.get_level(level_idx)

            safe_level = {
                'idx': level_idx,
                'name': level.name, 
                'summary': decision_problem.summary,
                'type': level.type,
                'description': level.description,
                'image': level.image,
                'questions': level.questions
                }

            emit('level_data', 
                {
                    'progress': player.progress,
                    'player_at_level_idx': player.current_level,
                    'level': safe_level
                },
                to=request.sid, # Only send to the user that has requested the data
                )
        except Exception as e:
            print(e)
            emit('error', 
                 {'message': f'Unexpected error occured: {e}'},
                 to=request.sid, # Only send to the user that has requested the data
                 )


    @socketio.on('submit_level')
    def handle_submit_level(data):
        try:
            print(f"handle submit_level {data}")

            game_session: GameSession = get_game_session(data['game_session_id'])
            player: Player = game_session.get_player(data["username"])
            decision_problem: DecisionProblem = game_session.decision_problem

            # Double check if player is done
            if player.current_level == decision_problem.nr_levels:
                player.set_finished()
                return
            
            level: DecisionProblemLevel = decision_problem.get_level(player.current_level)

            # Require for each question an answer
            submission = data.get('submission')
            print(submission)
            # Note: answers is a list with both the question and the answer in it like this:
            #    [{'question': ['What is the probability p1?', .25, ''], 'answer': '.25'}, ..]
         
            # Check if each answer is correct
            # This works for the Decision Tree, where we expect all answers to be numbers
            if submission is not None:
                for s in submission:
                    print(s)
                    question = s['question']['question']
                    hint = s['question']['hint']
                    answer = s['question']['answer']
                    submission = s['submission']

                    if level.type == 'NUMERIC':
                        answer = float(answer)
                        submission = float(submission)
                        print(answer, submission, abs(answer - submission) )
                        if (abs(answer - submission) > 0.01):
                            # Lower the score for each wrong try:
                            player.add_to_score(-1)
                            emit('wrong_answer', {'message': f'❌Wrong answer given for question \"{question}\"\n\n💡Hint: {hint}'})
                            return
                    
                    if level.type == 'OPTIONS':
                        if (answer != submission):
                            # Lower the score for each wrong try:
                            player.add_to_score(-1)
                            emit('wrong_answer', {'message': f'❌Wrong answer given for question \"{question}\"\n\n💡Hint: {hint}'})
                            return
            
            # Increase the score for the player
            player.add_to_score(level.score)

            # Move to next level
            player.next_level()

            # Check if player is done
            if player.current_level == decision_problem.nr_levels:
                player.set_finished()

            # Update the leader board
            leaderboard = game_session.get_leaderboard()
            emit('leaderboard_data', {'leaderboard': leaderboard}, room=game_session.id)

            # Let the player know he needs the next level
            emit('game_data_refresh_needed', 
                to=request.sid, # Only send to the user that has requested the data
            )
        
        except Exception as e:
            emit('error', 
                 {'message': f'Unexpected error occured: {e}'},
                 to=request.sid, # Only send to the user that has requested the data
                 )
