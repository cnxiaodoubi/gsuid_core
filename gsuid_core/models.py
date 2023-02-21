from typing import Any, List, Literal, Optional

from msgspec import Struct


class Message(Struct):
    type: Optional[str] = None
    data: Optional[Any] = None


class MessageReceive(Struct, frozen=True):
    bot_id: str = 'Bot'
    user_type: Optional[
        Literal['group', 'direct', 'channel', 'sub_channel']
    ] = None
    group_id: Optional[str] = None
    user_id: str = ''
    user_pm: int = 3
    content: List[Message] = []


class MessageContent(Struct):
    raw: MessageReceive = MessageReceive()
    raw_text: str = ''
    command: str = ''
    text: str = ''
    image: Optional[str] = None
    at: Optional[str] = None
    image_list: List[Any] = []
    at_list: List[Any] = []


class MessageSend(Struct):
    bot_id: str = 'Bot'
    target_type: Optional[str] = None
    target_id: Optional[str] = None
    content: Optional[List[Message]] = None
