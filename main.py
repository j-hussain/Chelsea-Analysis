import pandas as pd
import streamlit as st


def main():


    df = pd.read_csv('data.csv')
    df = df[:25]

    # Remove goalkeepers as they don't really play a role in creation and attack

    df = df.loc[df['Pos'] != 'GK']
    df.reset_index()

    df['Min'] = pd.to_numeric(df['Min'].str.replace(',', ''))

    df['XG_diff'] = df['Gls90'] - df['xG90']
    df['XA_diff'] = df['Ast90'] - df['xA90']
    df['MinPerGoal'] = df['Min'] / df['Gls']

    df.columns = df.columns.str.strip()

    df = df.sort_values('XG_diff', axis=0, ascending=False)

    uA = df.head()

    st.write("Here's some data!")
    st.write(uA)

if __name__ == "__main__":
    main()