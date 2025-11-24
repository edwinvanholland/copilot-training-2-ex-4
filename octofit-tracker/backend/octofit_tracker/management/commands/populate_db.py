from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

# Minimal models for direct DB access (for demo purposes)
from django.db import connection

def get_collection(name):
    return connection.cursor().db_conn[name]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Populating octofit_db with test data...'))
        db = connection.cursor().db_conn

        # Collections
        users = db['users']
        teams = db['teams']
        activities = db['activities']
        leaderboard = db['leaderboard']
        workouts = db['workouts']

        # Clear collections
        users.delete_many({})
        teams.delete_many({})
        activities.delete_many({})
        leaderboard.delete_many({})
        workouts.delete_many({})

        # Teams
        marvel = {'name': 'Marvel', 'members': []}
        dc = {'name': 'DC', 'members': []}
        teams.insert_many([marvel, dc])

        # Users
        user_data = [
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': 'Marvel'},
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'DC'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'DC'},
        ]
        users.insert_many(user_data)

        # Activities
        activities.insert_many([
            {'user': 'Spider-Man', 'type': 'running', 'points': 50},
            {'user': 'Iron Man', 'type': 'strength', 'points': 70},
            {'user': 'Wonder Woman', 'type': 'walking', 'points': 30},
            {'user': 'Batman', 'type': 'strength', 'points': 60},
        ])

        # Workouts
        workouts.insert_many([
            {'user': 'Spider-Man', 'workout': 'Web Swinging', 'duration': 30},
            {'user': 'Iron Man', 'workout': 'Armor Training', 'duration': 45},
            {'user': 'Wonder Woman', 'workout': 'Lasso Practice', 'duration': 40},
            {'user': 'Batman', 'workout': 'Martial Arts', 'duration': 50},
        ])

        # Leaderboard
        leaderboard.insert_many([
            {'team': 'Marvel', 'points': 120},
            {'team': 'DC', 'points': 90},
        ])

        # Unique index on email
        users.create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))
