from django.db.models import QuerySet

from farmster_server.models.agent import Agent


def get_all_agents() -> QuerySet:
    return Agent.objects.all()


def get_agent_by_id(agent_id) -> Agent:
    return Agent.objects.get(id=agent_id)
