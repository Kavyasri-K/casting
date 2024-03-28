import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from api import create_app
from database.models import setup_db, Actor, Movie, db

from dotenv import load_dotenv

load_dotenv()

DB_user = os.getenv('DB_user')
DB_host = os.getenv('DB_host')
DB_name = os.getenv('DB_name')
DB_password = os.getenv('DB_password')


class CastingTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(active=False)
        self.client = self.app.test_client
        self.database_name = 'postgres'
        self.database_path = 'postgresql://{}:{}@{}/{}'.format(
            DB_user, DB_password, DB_host, self.database_name)
        setup_db(self.app)
        self.token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlNub24zeFAwRE1NTERxdzd0cEppNSJ9.eyJpc3MiOiJodHRwczovL2thdnlhc3Jpay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjVmYzYyYmQ4OWVlYmM0YjgyZjJkNTQzIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTcxMTY0ODM1MiwiZXhwIjoxNzExNjU1NTUyLCJzY29wZSI6IiIsImF6cCI6IlF3d0xTVDlCckQ3Vm9leWhNNzczbDJzVDdvMXY0TGpnIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.ZYSAcJ9QPuv8lpHTLXx2AmOeEDMGiNuizK-JQRCMCtj216ynMDUdOXZqcltOWdo_ZTaISmnN6t3XK30tt_0eOyq0O5LlOq9cpCO1MeheMK54BQgLirzdLVIs8BjfQd2uzYNsfbx1KuOEBTOWe7k6RG_fPd27nFCuRtVdUis03Jqx0jczKTY50re4LCxkF0NqcdPxj2p58p05Jl9h5L8T-yBQS91cNAzvYr1cxqYATjK_COq-sZGpUpj_F4LNSYiMD46UDH0D2TtF8B0os5coqx43mzYuLKEQpnH6Z_r6bEMTBRu2d9QufCmovafBBQXz1Zpyzf_NksKI-7kRmSZRNw'

        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token)
        }

        self.new_movie = {
            "title": "Billa",
            "release_date": "2017-05-16"
        }

        self.new_actor = {
            "name": "Goundamani",
            "age": 78,
            "gender": "Male"
        }

        self.movie_id_del = 2

        self.actor_id_del = 2

        self.updated_movie_data = {
            "title": "Update Movie",
            "release_date": "2022-01-01"
        }

        self.updated_actor_data = {
            "name": "Update Name",
            "age": 40,
            "gender": "Female"
        }

    def tearDown(self):
        # with self.app.app_context():
        #     db.drop_all()
        pass

    # ----------------------------------------
    # Movies
    # ----------------------------------------

    def test_get_movies_without_authentication(self):
        response = self.client().get('/movies')
        print(response)

        self.assertEqual(response.status_code, 500)

    def test_get_movies_with_authentication(self):
        response = self.client().get('/movies', headers=self.headers)
        print(response)

        self.assertEqual(response.status_code, 200)
        print(response.data)

    def test_post_movies_with_authentication(self):
        response = self.client().post(
            '/movies', json=self.new_movie, headers=self.headers)
        print(response)

        self.assertEqual(response.status_code, 201)

    def test_update_movie(self):
        movie_id = 1
        response = self.client().patch(
            f'/movies/{movie_id}', json=self.updated_movie_data, headers=self.headers)
        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertTrue(data['success'])

    def test_delete_movie(self):

        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        response = self.client().delete(
            f'/movies/{self.movie_id_del}', headers=headers)
        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertTrue(data['success'])

    # ----------------------------------------
    # Actors
    # ----------------------------------------

    def test_get_actors_without_authentication(self):
        response = self.client().get('/actors')
        print(response)

        self.assertEqual(response.status_code, 401)

    def test_get_actors_with_authentication(self):
        response = self.client().get('/actors', headers=self.headers)
        print(response)

        self.assertEqual(response.status_code, 200)
        print(response.data)

    def test_post_actors_with_authentication(self):

        response = self.client().post(
            '/actors', json=self.new_actor, headers=self.headers)
        print(response)

        self.assertEqual(response.status_code, 201)

    def test_update_actor(self):
        actor_id = 1
        response = self.client().patch(
            f'/actors/{actor_id}', json=self.updated_actor_data, headers=self.headers)
        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertTrue(data['success'])

    def test_delete_actor(self):

        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }
        response = self.client().delete(
            f'/actors/{self.actor_id_del}', headers=headers)
        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertTrue(data['success'])


if __name__ == "__main__":
    unittest.main(exit=False)
