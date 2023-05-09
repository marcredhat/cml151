
#https://towardsdatascience.com/stable-diffusion-using-hugging-face-501d8dbdd8

from diffusers import StableDiffusionPipeline
# Initialize a prompt
prompt = "a dog wearing hat"
# Pass the prompt in the pipeline
pipe(prompt).images[0]
