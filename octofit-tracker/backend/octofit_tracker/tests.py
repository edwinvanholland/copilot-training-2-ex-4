from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name='Test', email='test@example.com', team='Marvel')
        self.assertEqual(user.name, 'Test')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team, 'Marvel')

    def test_team_creation(self):
        team = Team.objects.create(name='Marvel', members=[])
        self.assertEqual(team.name, 'Marvel')
        self.assertEqual(team.members, [])

    def test_activity_creation(self):
        activity = Activity.objects.create(user='Test', type='running', points=10)
        self.assertEqual(activity.user, 'Test')
        self.assertEqual(activity.type, 'running')
        self.assertEqual(activity.points, 10)

    def test_workout_creation(self):
        workout = Workout.objects.create(user='Test', workout='Pushups', duration=20)
        self.assertEqual(workout.user, 'Test')
        self.assertEqual(workout.workout, 'Pushups')
        self.assertEqual(workout.duration, 20)

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='Marvel', points=100)
        self.assertEqual(lb.team, 'Marvel')
        self.assertEqual(lb.points, 100)
