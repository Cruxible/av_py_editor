#!/usr/bin/env python3

#Author: Ioannes Cruxibulum
#Sep.10th 2023

#pip3 install yt-dlp
import platform
import os
import time
import getpass
import yt_dlp
from rich.tree import Tree
from rich import print
from rich.console import Console
from moviepy.editor import *
from moviepy.editor import VideoFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
import sys
import subprocess

class main_logo:
	def logo():
		print(" [red1]___  _   _ ____ ____\n |__]  \\_/  |__/ |__|\n |      |   |  \\ |  |[/red1]")

class HonerableMentions:
	mp4 = " [white]Please choose a mp4[/white]"
	mp3 = " [white]Please choose a mp3[/white]"
	starting_time = " [white]start time?[/white]"
	ending_time = " [white]End Time?[/white]"
	save_vid_where = " [white]Save on Desktop Videos or droid?[/white]"
	save_audio_where = " [white]Save on Desktop Music or droid?[/white]"
	old_filename = " [white]Filename?[/bright_black]"
	new_filename = " [white]New filename?[/white]"
	exit_program = " [white]Exiting the program...[/white]"

class MySexyVariables:
	video_dir = os.path.join(os.path.expanduser("~"), "Videos")
	audio_dir = os.path.join(os.path.expanduser("~"), "Music")
	desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")
	pics_dir = os.path.join(os.path.expanduser("~"), "Pictures")
	sd_video_dir = os.path.join("/sdcard", "Videos")
	sd_Music_dir = os.path.join("/sdcard", "Music")
	vid_list = os.listdir(video_dir)
	audio_list = os.listdir(audio_dir)
	desktop_list = os.listdir(desktop_dir)
	pics_list = os.listdir(pics_dir)
	calls_list = [
				"download",
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
		user = getpass.getuser()
		curdir = os.getcwd()
		console = Console()
		return console.input(" [white]_______________________________________________[/white]" + "[red]\n  __ [/red]" + "[white]" + curdir + " [/white]" + "[red]\n (__[/red]" + "[white]" + user + "[/white]" + "[red]__: [/red]")

	@staticmethod
	def get_integer_input():
		user = getpass.getuser()
		curdir = os.getcwd()
		console = Console()
		return int(console.input(" [white]_______________________________________________[/white]" + "[red]\n  __ [/red]" + "[white]" + curdir + " [/white]" + "[red]\n (__[/red]" + "[white]" + user + "[/white]" + "[red]__: [/red]"))

	@staticmethod
	def get_float_input():
		user = getpass.getuser()
		curdir = os.getcwd()
		console = Console()
		return float(console.input(" [white]_______________________________________________[/white]" + "[red]\n  __ [/red]" + "[white]" + curdir + " [/white]" + "[red]\n (__[/red]" + "[white]" + user + "[/white]" + "[red]__: [/red]"))

class calls:
	@staticmethod
	def call_list():
		tree = Tree("[white]" + " Editing Tools", guide_style= "red")
		for i in MySexyVariables.calls_list:
			tree.add("[white]" + str(i))
		print(" ", tree)

class list_dirs:
	@staticmethod
	def vid_list():
		os.chdir(MySexyVariables.video_dir)
		tree = Tree("[white]" + MySexyVariables.video_dir, guide_style="red")
		for i in MySexyVariables.vid_list:
			tree.add("[white]" + str(i))
		print(" ", tree)

	@staticmethod
	def music_list():
		os.chdir(MySexyVariables.audio_dir)
		tree = Tree("[white]" + MySexyVariables.audio_dir, guide_style="red")
		for i in MySexyVariables.audio_list:
			tree.add("[white]" + str(i))
		print(" ", tree)

	@staticmethod
	def desktop_list():
		os.chdir(MySexyVariables.desktop_dir)
		tree = Tree("[white]" + MySexyVariables.desktop_dir, guide_style="red")
		for i in MySexyVariables.desktop_list:
			tree.add("[white]" + str(i))
		print(" ", tree)

	@staticmethod
	def picture_list():
		os.chdir(MySexyVariables.pics_dir)
		tree = Tree("[white]" + MySexyVariables.pics_dir, guide_style="red")
		for i in MySexyVariables.pics_list:
			tree.add("[white]" + str(i))
		print(" ", tree)

class main_functions:
	def download_video():
		def download_call():
			print(' [white]How would you like to download?[/white]')
			list_choice = ['mp3', 'best video', 'choose format']
			tree = Tree("[white]" + MySexyVariables.pics_dir, guide_style="red")
			for i in list_choice:
				tree.add("[white]" + str(i))
			print(" ", tree)
			video_format = Input.get_string_input()
			if video_format == 'mp3':
				print(' [white]Please enter a link[/white]')
				url = Input.get_string_input()
				mp3_command = f"yt-dlp -x --audio-format mp3 {url}"
				os.system(mp3_command)
			elif video_format == 'best video':
				print(' [white]Please enter a link[/white]')
				url = Input.get_string_input()
				best_video_command = f'yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]" -o video.mp4 "{url}"'
				os.system(best_video_command)
			elif video_format == 'choose format':
				print(' [white]Please enter a link[/white]')
				url = Input.get_string_input()
				format_command = f"yt-dlp -F {url}"
				output = subprocess.check_output(format_command, shell=True).decode()
				print(output)
				print(' [white]Enter the format code.\n code 22 or 18 is common.[/white]')
				format = Input.get_integer_input()
				format_code_command = f"yt-dlp -f {format} {url}"
				os.system(format_code_command)
			elif video_format == 'exit':
				sys.exit()

		print(HonerableMentions.save_vid_where)
		directory = Input.get_string_input()
		if directory == 'Desktop':
			os.chdir(MySexyVariables.desktop_dir)
			download_call()
		elif directory == 'Videos':
			os.chdir(MySexyVariables.video_dir)
			download_call()
		elif directory == 'droid':
			os.chdir(MySexyVariables.sd_video_dir)
			download_call()
		elif directory == MySexyVariables.calls_list[6]:
			sys.exit()


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
				audio = audio.subclip(audio_begining, video.duration)
				final = video.set_audio(audio)
				print(HonerableMentions.save_vid_where)
				directory = Input.get_string_input()
				if directory == 'Desktop':
					os.chdir(MySexyVariables.desktop_dir)
					print(HonerableMentions.new_filename)
					new_file = Input.get_string_input()
					final.write_videofile(f"{new_file}")
				elif directory == 'Videos':
					os.chdir(MySexyVariables.video_dir)
					print(HonerableMentions.new_filename)
					new_file = Input.get_string_input()
					final.write_videofile(f"{new_file}")
				elif directory == 'droid':
					os.chdir(MySexyVariables.sd_video_dir)
					print(HonerableMentions.new_filename)
					new_file = Input.get_string_input()
					final.write_videofile(f"{new_file}")
				elif directory == MySexyVariables.calls_list[6]:
					sys.exit()
			if audio_file == MySexyVariables.calls_list[6]:
				sys.exit()
		if video_file == MySexyVariables.calls_list[6]:
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
			elif directory == 'Music':
				os.chdir(MySexyVariables.audio_dir)
				new_audio.write_audiofile(output_file_path)
			elif directory == 'droid':
				os.chdir(MySexyVariables.sd_Music_dir)
				new_audio.write_audiofile(output_file_path)
			elif directory == MySexyVariables.calls_list[6]:
				sys.exit()
		if filename == MySexyVariables.calls_list[6]:
			sys.exit()

	def volume_adjust():
		list_dirs.vid_list()
		print(HonerableMentions.mp4)
		filename = Input.get_string_input()
		if filename in MySexyVariables.vid_list:
			def get_float_input():
			    user_input = Input.get_string_input()
			    if user_input.lower() == 'exit':
			        return -1
			    else:
			        return float(user_input)
			print(' [white]Enter the final volume.\n You can set vol_num to 0.5 for half\n Type \'exit\' to quit.[/white]')
			vol_num = get_float_input()
			if vol_num == -1:
			    print(HonerableMentions.exit_program)
			    sys.exit()
			print(' [white]Enter the fade duration.\n You can set fade_duration to 5.0\n Type \'exit\' to quit.[/white]')
			fade_duration = get_float_input()
			if fade_duration == -1:
			    print(HonerableMentions.exit_program)
			    sys.exit()
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
			elif directory == 'Videos':
				os.chdir(MySexyVariables.video_dir)
				clip.write_videofile(new_file)
			elif directory == 'droid':
				os.chdir(MySexyVariables.sd_video_dir)
				clip.write_videofile(new_file)
			elif directory == MySexyVariables.calls_list[6]:
				sys.exit()
		if filename == MySexyVariables.calls_list[6]:
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
			elif directory == 'Videos':
				os.chdir(MySexyVariables.video_dir)
				clip.write_videofile(new_vid_name)
			elif directory == 'droid':
				os.chdir(MySexyVariables.sd_video_dir)
				clip.write_videofile(new_vid_name)
			elif directory == MySexyVariables.calls_list[6]:
				sys.exit()
		if vid_name == MySexyVariables.calls_list[6]:
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
			elif directory == 'Music':
				os.chdir(MySexyVariables.audio_dir)
				audio.write_audiofile(new_filename)
			elif directory == 'droid':
				os.chdir(MySexyVariables.sd_Music_dir)
				audio.write_audiofile(new_filename)
			elif directory == MySexyVariables.calls_list[6]:
				sys.exit()
		if filename == MySexyVariables.calls_list[6]:
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
				elif directory == 'Music':
					os.chdir(MySexyVariables.audio_dir)
					final_audio.write_audiofile(new_file)
				elif directory == 'droid':
					os.chdir(MySexyVariables.sd_Music_dir)
					final_audio.write_audiofile(new_file)
				elif directory == MySexyVariables.calls_list[6]:
					sys.exit()
			if second_file == MySexyVariables.calls_list[6]:
				sys.exit()
		if first_file == MySexyVariables.calls_list[6]:
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
				elif directory == 'Videos':
					os.chdir(MySexyVariables.video_dir)
					final_video.write_videofile(new_file)
				elif directory == 'droid':
					os.chdir(MySexyVariables.sd_video_dir)
					final_video.write_videofile(new_file)
				elif directory == MySexyVariables.calls_list[6]:
					sys.exit()
			if second_file == MySexyVariables.calls_list[6]:
				sys.exit()
		if first_file == MySexyVariables.calls_list[6]:
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
					main_functions.download_video()
					os.system('clear')
					Main.main()
				elif command == MySexyVariables.calls_list[1]:
					main_functions.cut_vid()
					os.system('clear')
					Main.main()
				elif command == MySexyVariables.calls_list[2]:
					main_functions.cut_mp3()
					os.system('clear')
					Main.main()
				elif command == MySexyVariables.calls_list[3]:
					main_functions.volume_adjust()
					os.system('clear')
					Main.main()
				elif command == MySexyVariables.calls_list[4]:
					main_functions.over_lay()
					os.system('clear')
					Main.main()
				elif command == MySexyVariables.calls_list[5]:
					main_functions.ext_audio()
					os.system('clear')
					Main.main()
				elif command == MySexyVariables.calls_list[6]:
					main_functions.concatenate_mp3()
					os.system('clear')
					Main.main()
				elif command == MySexyVariables.calls_list[7]:
					main_functions.concatenate_videos()
					os.system('clear')
					Main.main()
				elif command == MySexyVariables.calls_list[8]:
					sys.exit()
				elif command == 'list':
					list_dirs.vid_list()
					list_dirs.music_list()
					list_dirs.desktop_list()
					list_dirs.picture_list()
					os.system('clear')
					Main.main()
				else:
					continue
		else:
			print(' I use sparky linux btw.')

if __name__ == '__main__':
	print(f" [white]System: {platform.system()}\n Node Name: {platform.node()}\n Release: {platform.release()}[/white]")
	print(f" [white]Version: {platform.version()}\n Machine: {platform.machine()}\n Python version: {platform.python_version()}/white]")
	print(" [red1]All that we see or seem is but a dream within a dream\n ~ Edgar Allen Poe[/red1]")
	if platform.system() == 'Linux':
		Main.main()

