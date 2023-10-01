import platform
import os
import time
import getpass
from rich.tree import Tree
from rich import print
from rich.console import Console
from moviepy.editor import *
from moviepy.editor import VideoFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
import sys

class main_logo:
	def logo():
		print(" [red1]___  _   _ ____ ____\n |__]  \\_/  |__/ |__|\n |      |   |  \\ |  |[/red1]\n")

class HonerableMentions:
	mp4 = " Please choose a mp4"
	mp3 = " Please choose a mp3"
	starting_time = " start time?"
	ending_time = " End Time?"
	save_vid_where = " Save on Desktop or in Videos?"
	save_audio_where = " Save on Desktop or in Music?"
	old_filename = " Filename?"
	new_filename = " New filename?"

class MySexyVariables:
	user = getpass.getuser()
	curdir = os.getcwd()
	video_dir = os.path.join(os.path.expanduser("~"), "Videos")
	audio_dir = os.path.join(os.path.expanduser("~"), "Music")
	desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")
	pics_dir = os.path.join(os.path.expanduser("~"), "Pictures")
	vid_list = os.listdir(video_dir)
	audio_list = os.listdir(audio_dir)
	desktop_list = os.listdir(desktop_dir)
	pics_list = os.listdir(pics_dir)
	calls_list = [
				"cut video",
				"cut audio",
				"adjust volume",
				"audio overlay",
				"extract audio",
				"stitch audio",
				"stitch video",
				"exit"
				]

class Input:
    @staticmethod
    def get_string_input():
        console = Console()
        return console.input(" [bright_black]_______________________________________________[/bright_black]" + "[bright_black]\n  __ [/bright_black]" + "[red1]" + MySexyVariables.curdir + " [/red1]" + "[bright_black]\n (____ [/bright_black]" + "[purple]" + MySexyVariables.user + "[/purple]" + "[bright_black] _____: [/bright_black]")
    
    @staticmethod
    def get_integer_input():
        console = Console()
        return int(console.input(" [bright_black]_______________________________________________[/bright_black]" + "[bright_black]\n  __ [/bright_black]" + "[red1]" + MySexyVariables.curdir + " [/red1]" + "[bright_black]\n (____ [/bright_black]" + "[purple]" + MySexyVariables.user + "[/purple]" + "[bright_black] _____: [/bright_black]"))

    @staticmethod
    def get_float_input():
        console = Console()
        return float(console.input(" [bright_black]_______________________________________________[/bright_black]" + "[bright_black]\n  __ [/bright_black]" + "[red1]" + MySexyVariables.curdir + " [/red1]" + "[bright_black]\n (____ [/bright_black]" + "[purple]" + MySexyVariables.user + "[/purple]" + "[bright_black] _____: [/bright_black]"))

class calls:
	@staticmethod
	def call_list():
		tree = Tree("[bright_black]" + " calls", guide_style="purple")
		for i in MySexyVariables.calls_list:
			tree.add("[bright_black]" + str(i))
		print(" ", tree)

class list_dirs:
    @staticmethod
    def vid_list():
        os.chdir(MySexyVariables.video_dir)
        tree = Tree("[bright_black]" + MySexyVariables.video_dir, guide_style="purple")
        for i in MySexyVariables.vid_list:
            tree.add("[bright_black]" + str(i))
        print(" ", tree)

    @staticmethod
    def music_list():
        os.chdir(MySexyVariables.audio_dir)
        tree = Tree("[bright_black]" + MySexyVariables.audio_dir, guide_style="purple")
        for i in MySexyVariables.audio_list:
            tree.add("[bright_black]" + str(i))
        print(" ", tree)

    @staticmethod
    def desktop_list():
        os.chdir(MySexyVariables.desktop_dir)
        tree = Tree("[bright_black]" + MySexyVariables.desktop_dir, guide_style="purple")
        for i in MySexyVariables.desktop_list:
            tree.add("[bright_black]" + str(i))
        print(" ", tree)

    @staticmethod
    def picture_list():
        os.chdir(MySexyVariables.pics_dir)
        tree = Tree("[bright_black]" + MySexyVariables.pics_dir, guide_style="purple")
        for i in MySexyVariables.pics_list:
            tree.add("[bright_black]" + str(i))
        print(" ", tree)

class main_functions:
    def over_lay():
    	list_dirs.vid_list()
    	print(HonerableMentions.mp4)
    	video_file = Input.get_string_input()
    	if video_file in MySexyVariables.vid_list:
    		video = VideoFileClip(f"{video_file}")
    		list_dirs.music_list()
    		print(HonerableMentions.mp3)
    		audio_file = Input.get_string_input()
    		if audio_file in MySexyVariables.audio_list:
    			audio = AudioFileClip(f"{audio_file}")
    			print(HonerableMentions.starting_time)
    			audio_begining = Input.get_integer_input()
    			# Cut audio to the length of the video
    			audio = audio.subclip(audio_begining, video.duration)
    			final = video.set_audio(audio)
    			print(HonerableMentions.save_vid_where)
    			directory = Input.get_string_input()
    			if directory == 'Desktop':
    				os.chdir(MySexyVariables.desktop_dir)
    				print(HonerableMentions.new_filename)
    				new_file = Input.get_string_input()
    				final.write_videofile(f"{new_file}")
    			if directory == 'Videos':
    				os.chdir(MySexyVariables.video_dir)
    				print(HonerableMentions.new_filename)
    				new_file = Input.get_string_input()
    				final.write_videofile(f"{new_file}")
    			if "exit" == directory:
    				sys.exit()
    		if "exit" == audio_file:
    			sys.exit()
    	if "exit" == video_file:
    		sys.exit()

    def cut_mp3():
    	list_dirs.music_list()
    	print(HonerableMentions.mp3)
    	filename = Input.get_string_input()
    	if filename in MySexyVariables.audio_list:
    		print(HonerableMentions.starting_time)
    		start_time = Input.get_integer_input()
    		print(HonerableMentions.ending_time)
    		end_time = Input.get_integer_input()
    		print(HonerableMentions.new_filename)
    		output_file_path = Input.get_string_input()
    		print(HonerableMentions.save_audio_where)
    		directory = Input.get_string_input()
    		audio = AudioFileClip(filename)
    		new_audio = audio.subclip(start_time, end_time)
    		if directory == 'Desktop':
    			os.chdir(MySexyVariables.desktop_dir)
    			new_audio.write_audiofile(output_file_path)
    		if directory == 'Music':
    			os.chdir(MySexyVariables.audio_dir)
    			new_audio.write_audiofile(output_file_path)
    		if "exit" == directory:
    			sys.exit()
    	if "exit" == filename:
    		sys.exit()

    def volume_adjust():
    	list_dirs.vid_list()
    	print(HonerableMentions.mp4)
    	filename = Input.get_string_input()
    	if filename in MySexyVariables.vid_list:
    		print(' Enter the final volume"')
    		vol_num = Input.get_float_input()
    		print(' Enter the fade duration?')
    		fade_duration = Input.get_float_input()
    		clip = VideoFileClip(filename)
    		clip = clip.volumex(vol_num)
    		clip = clip.audio_fadein(fade_duration)
    		clip = clip.audio_fadeout(fade_duration)
    		print(HonerableMentions.new_filename)
    		new_file = Input.get_string_input()
    		print(HonerableMentions.save_vid_where)
    		directory = Input.get_string_input()
    		if directory == 'Desktop':
    			os.chdir(MySexyVariables.desktop_dir)
    			clip.write_videofile(new_file)
    		if directory == 'Videos':
    			os.chdir(MySexyVariables.video_dir)
    			clip.write_videofile(new_file)
    		if "exit" == directory:
    			sys.exit()
    	if "exit" == filename:
    		sys.exit()
    
    def cut_vid():
    	list_dirs.vid_list()
    	print(HonerableMentions.mp4)
    	vid_name = Input.get_string_input()
    	if vid_name in MySexyVariables.vid_list:
    		print(HonerableMentions.starting_time)
    		start_time = Input.get_integer_input()
    		print(HonerableMentions.ending_time)
    		end_time = Input.get_integer_input()
    		print(HonerableMentions.new_filename)
    		new_vid_name = Input.get_string_input()
    		clip = VideoFileClip(vid_name).subclip(start_time, end_time)
    		print(HonerableMentions.save_vid_where)
    		directory = Input.get_string_input()
    		if directory == 'Desktop':
    			os.chdir(MySexyVariables.desktop_dir)
    			clip.write_videofile(new_vid_name)
    		if directory == 'Videos':
    			os.chdir(MySexyVariables.video_dir)
    			clip.write_videofile(new_vid_name)
    		if "exit" == directory:
    			sys.exit()
    	if "exit" == vid_name:
    		sys.exit()

    def ext_audio():
    	list_dirs.vid_list()
    	print(HonerableMentions.mp4)
    	filename = Input.get_string_input()
    	if filename in MySexyVariables.vid_list:
    		print(HonerableMentions.new_filename)
    		new_filename = Input.get_string_input()
    		video = VideoFileClip(filename)
    		audio = video.audio
    		print(HonerableMentions.save_audio_where)
    		directory = Input.get_string_input()
    		if directory == 'Desktop':
    			os.chdir(MySexyVariables.desktop_dir)
    			audio.write_audiofile(new_filename)
    		if directory == 'Music':
    			os.chdir(MySexyVariables.audio_dir)
    			audio.write_audiofile(new_filename)
    		if "exit" == directory:
    			sys.exit()
    	if "exit" == filename:
    		sys.exit()
    
    def concatenate_mp3():
    	list_dirs.music_list()
    	print(HonerableMentions.mp3)
    	first_file = Input.get_string_input()
    	if first_file in MySexyVariables.audio_list:
    		second_file = Input.get_string_input()
    		if second_file in MySexyVariables.audio_list:
    			audio1 = AudioFileClip(first_file)
    			audio2 = AudioFileClip(second_file)
    			final_audio = concatenate_audioclips([audio1, audio2])
    			print(HonerableMentions.new_filename)
    			new_file = Input.get_string_input()
    			print(HonerableMentions.save_audio_where)
    			directory = Input.get_string_input()
    			if directory == 'Desktop':
    				os.chdir(MySexyVariables.desktop_dir)
    				final_audio.write_audiofile(new_file)
    			if directory == 'Music':
    				os.chdir(MySexyVariables.audio_dir)
    				final_audio.write_audiofile(new_file)
    			if "exit" == directory:
    				sys.exit()
    		if "exit" == second_file:
    			sys.exit()
    	if "exit" == first_file:
    		sys.exit()
    
    def concatenate_videos():
    	list_dirs.vid_list()
    	print(HonerableMentions.mp4)
    	first_file = Input.get_string_input()
    	if first_file in MySexyVariables.vid_list:
    		print(HonerableMentions.mp4)
    		second_file = Input.get_string_input()
    		if second_file in MySexyVariables.vid_list:
    			video1 = VideoFileClip(first_file)
    			video2 = VideoFileClip(second_file)
    			final_video = concatenate_videoclips([video1, video2])
    			print(HonerableMentions.new_filename)
    			new_file = Input.get_string_input()
    			print(HonerableMentions.save_vid_where)
    			directory = Input.get_string_input()
    			if directory == 'Desktop':
    				os.chdir(MySexyVariables.desktop_dir)
    				final_video.write_videofile(new_file)
    			if directory == 'Videos':
    				os.chdir(MySexyVariables.video_dir)
    				final_video.write_videofile(new_file)
    			if "exit" == directory:
    				sys.exit()
    		if "exit" == second_file:
    			sys.exit()
    	if "exit" == first_file:
    		sys.exit()

class Main:
	def main():
		if platform.system() == 'Linux':
			time.sleep(2)
			main_logo.logo()
			calls.call_list()
			while True:
				command = Input.get_string_input()
				if command == MySexyVariables.calls_list[0]:
					main_functions.cut_vid()
					main_logo.logo()
					os.system('clear')
					Main.main()
				if command == MySexyVariables.calls_list[1]:
					main_functions.cut_mp3()
					main_logo.logo()
					os.system('clear')
					Main.main()
				if command == MySexyVariables.calls_list[2]:
					main_functions.volume_adjust()
					main_logo.logo()
					os.system('clear')
					Main.main()
				if command == MySexyVariables.calls_list[3]:
					main_functions.over_lay()
					main_logo.logo()
					os.system('clear')
					Main.main()
				if command == MySexyVariables.calls_list[4]:
					main_functions.ext_audio()
					main_logo.logo()
					os.system('clear')
					Main.main()
				if command == MySexyVariables.calls_list[5]:
					main_functions.concatenate_mp3()
					main_logo.logo()
					os.system('clear')
					Main.main()
				if command == MySexyVariables.calls_list[6]:
					main_functions.concatenate_videos()
					main_logo.logo()
					os.system('clear')
					Main.main()
				if command == MySexyVariables.calls_list[7]:
					sys.exit()
				if command == 'list':
					list_dirs.vid_list()
					list_dirs.music_list()
					list_dirs.desktop_list()
					list_dirs.picture_list()
					os.system('clear')
					Main.main()	
				else:
					continue
		else:
			print(' Your Mom don\'t use Linux Bruh!')

if __name__ == '__main__':
	print(f" [purple]System: {platform.system()}\n Node Name: {platform.node()}\n Release: {platform.release()}[/purple]")
	print(f" [purple]Version: {platform.version()}\n Machine: {platform.machine()}\n Python version: {platform.python_version()}[purple]")
	print(" [red1]All that we see or seem is but a dream within a dream\n ~ Edgar Allen Poe[/red1]")
	Main.main()