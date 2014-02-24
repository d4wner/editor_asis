#! /usr/bin/env python
# coding=utf-8

def red(param):
	result = "\x1B[0;31;40m"+param+"\x1B[0m"
	return result

def green(param):
	result = "\x1B[0;32;40m"+param+"\x1B[0m"
	return result

def yellow(param):
	result = "\x1B[0;33;40m"+param+"\x1B[0m"
	return result

def blue(param):
	result = "\x1B[0;34;40m"+param+"\x1B[0m"
	return result
