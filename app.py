"""Streamlit entrypoint: verify Supabase client initialization."""

import streamlit as st

from db_connection import supabase

st.set_page_config(page_title="Task App", layout="centered")
st.title("Task App")

if supabase is not None:
    st.success("Supabase client initialized successfully.")
else:
    st.warning(
        "Supabase client is not configured. Set `SUPABASE_URL` and `SUPABASE_KEY` in your `.env` file."
    )
