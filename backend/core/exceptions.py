class EduAgentBaseError(Exception):
    def __init__(self,message:str,agent_type:str="",details:dict=None):
        super().__init__(message)
        self.agent_type = agent_type
        self.details = details or {}
class LLMAPIError(EduAgentBaseError):
    pass
class AgentExecutionError(EduAgentBaseError):
    pass
class PipelineError(EduAgentBaseError):
    pass
class IntentRouteError(EduAgentBaseError):
    pass
class MilvusConnectionError(EduAgentBaseError):
    pass
class FileParseError(EduAgentBaseError):
    pass
class InvalidInputError(EduAgentBaseError):
    pass
class AuthenticationError(EduAgentBaseError):
    pass