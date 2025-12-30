import os
from supabase import create_client
from dotenv import load_dotenv

class ConexionDB:
    def __init__(self):
        load_dotenv()

    def conexionSupabase(self):
        url =  os.getenv("SUPABASE_URL")
        apiKey = os.getenv("SUPABASE_APIKEY")
        supabase = create_client(url,apiKey)

        return supabase

objetoPrueba = ConexionDB()
print(objetoPrueba.conexionSupabase)