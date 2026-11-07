import os
vari1 = input("File path: ")
vari2 = input("What shall the corruption size be? (The lower, the more corrupted): ")
vari3 = input("What is the output file path: ")

os.system(f"ffmpeg -i {vari1} -ar 64000 -c:a pcm_alaw -bsf noise={vari2} {vari3} ")