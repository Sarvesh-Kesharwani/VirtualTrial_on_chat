from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained("yisol/IDM-VTON")
prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
image = pipe(prompt).images[0]


from typing import Final 

TOKEN: Final = '7709502643:AAHtbgPqzYvJjkWly3dGhf7zAFKvztfRUYs'
Bo