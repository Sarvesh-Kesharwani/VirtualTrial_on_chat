from diffusers import DiffusionPipeline
import torch

pipe = DiffusionPipeline.from_pretrained("yisol/IDM-VTON")
pipeline.to("cuda")
prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
image = pipe(prompt).images[0]


pipeline = DiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipeline("An image of a squirrel in Picasso style").images[0]