#https://towardsdatascience.com/stable-diffusion-using-hugging-face-501d8dbdd8

from diffusers import StableDiffusionPipeline
pipe = StableDiffusionPipeline.from_pretrained('CompVis/stable-diffusion-v1-4').to('cuda')
# Initialize a prompt
prompt = "a monkey wearing hat"
# Pass the prompt in the pipeline
pipe(prompt).images[0]
