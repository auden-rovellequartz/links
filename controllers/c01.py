# -*- coding: utf-8 -*-

def home():
	page_one = A(
		"page_one",
		_href = URL(
			a = "links",
			c = "c01",
			f = "page_one",
			)
		)
	page_two = A(
		"page_two",
		_href = URL(
			a = "links",
			c = "c01",
			f = "page_two",
			)
		)
	return dict(
		page_one = page_one,
		page_two = page_two,
		)
def page_one():
	message = "You are on page #1!!!"
	home = A(
		"home",
		_href = URL(
			a = "links",
			c = "c01",
			f = "home",
			)
		)
	return dict(
		home = home,
		message = message,
		)
def page_two():
	message = "You are on page #2!!!"
	home = A(
		"home",
		_href = URL(
			a = "links",
			c = "c01",
			f = "home",
			)
		)
	return dict(
		home = home,
		message = message,
		)
