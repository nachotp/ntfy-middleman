
from ntfy_wrapper import NtfyPublisher

from ntfy_secrets import *

ntfy = NtfyPublisher(NTFY_DOMAIN, NTFY_TOPIC, NTFY_USER, NTFY_PASS)
ntfy.post("hola")