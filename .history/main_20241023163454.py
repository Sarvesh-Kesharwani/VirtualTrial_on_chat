from diffusers import DiffusionPipeline
import torch

pipe = DiffusionPipeline.from_pretrained("yisol/IDM-VTON")
prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
image = pipe(prompt).images[0]


pipeline("An image of a squirrel in Picasso style").images[0]