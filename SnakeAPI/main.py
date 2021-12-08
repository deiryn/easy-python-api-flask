from flask import *
import json
import os
import random

snake_path = 'D:\\pythonProjects\\SnakeAPI\\images'

snake_files = os.listdir(snake_path)

snake_list =[str(f) for f in snake_files]

app = Flask(__name__)

@app.route('/snake/', methods=['GET'])
def snake():
	shuffled = random.sample(snake_list, 1)
	snake_image = shuffled[0]
	data_set = {
				f'image': f'{snake_image}'
				}
	json_dump = json.dumps(data_set)

	return json_dump


if __name__ == '__main__':
	app.run(port=7777)