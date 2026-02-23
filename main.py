# Example Usage of Saya AI Agent

# Import the Saya AI module
from saya import SayaAI

# Initialize the AI agent
agent = SayaAI(api_key='YOUR_API_KEY_HERE')

# Example function to query the agent
def query_agent(query):
    response = agent.ask(query)
    print("Response from Saya AI:", response)

# Main usage: querying
if __name__ == '__main__':
    user_query = input("Enter your query for Saya AI: ")
    query_agent(user_query)