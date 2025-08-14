{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "992d966f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from agents import Agent, run_demo_loop, trace\n",
    "from dotenv import load_dotenv\n",
    "load_dotenv()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9593d5ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "with trace(\"doom_loop\"):\n",
    "    agent = Agent(name=\"Assistant\", instructions=\"You are a helpful assistant.\")\n",
    "    await run_demo_loop(agent)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "55a38407",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "openai_agent_sdk",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
