from .elem import Elem, Text

class Html(Elem):
	"""docstring for ."""
	def __init__(self, content=None, attr={}):
		"""
		__init__() method.

		Obviously.
		"""
		super().__init__(content=content, tag='html', attr=attr, tag_type='double')

class Head(Elem):
	"""docstring for ."""
	def __init__(self, content=None, attr={}):
		"""
		__init__() method.

		Obviously.
		"""
		super().__init__(content=content, tag='head', attr=attr, tag_type='double')

class Body(Elem):
	"""docstring for ."""
	def __init__(self, content=None, attr={}):
		"""
		__init__() method.

		Obviously.
		"""
		super().__init__(content=content, tag='body', attr=attr, tag_type='double')

class Title(Elem):
	"""docstring for ."""
	def __init__(self, content=None, attr={}):
		"""
		__init__() method.

		Obviously.
		"""
		super().__init__(content=content, tag='title', attr=attr, tag_type='double')

class Meta(Elem):
	"""docstring for ."""
	def __init__(self, content=None, attr={}):
		"""
		__init__() method.

		Obviously.
		"""
		super().__init__(content=content, tag='meta', attr=attr, tag_type='simple')

class Img(Elem):
	"""docstring for ."""
	def __init__(self, content=None, attr={}):
		"""
		__init__() method.

		Obviously.
		"""
		super().__init__(content=content, tag='img', attr=attr, tag_type='simple')

class Table(Elem):
	"""docstring for ."""
	def __init__(self, content=None, attr={}):
		"""
		__init__() method.

		Obviously.
		"""
		super().__init__(content=content, tag='table', attr=attr, tag_type='double')

class Th(Elem):
	"""docstring for ."""
	def __init__(self, content=None, attr={}):
		"""
		__init__() method.

		Obviously.
		"""
		super().__init__(content=content, tag='th', attr=attr, tag_type='double')

class Tr(Elem):
	"""docstring for ."""
	def __init__(self, content=None, attr={}):
		"""
		__init__() method.

		Obviously.
		"""
		super().__init__(content=content, tag='tr', attr=attr, tag_type='double')

class Td(Elem):
	"""docstring for ."""
	def __init__(self, content=None, attr={}):
		"""
		__init__() method.

		Obviously.
		"""
		super().__init__(content=content, tag='td', attr=attr, tag_type='double')

class Ul(Elem):
	"""docstring for ."""
	def __init__(self, content=None, attr={}):
		"""
		__init__() method.

		Obviously.
		"""
		super().__init__(content=content, tag='ul', attr=attr, tag_type='double')

class Ol(Elem):
	"""docstring for ."""
	def __init__(self, content=None, attr={}):
		"""
		__init__() method.

		Obviously.
		"""
		super().__init__(content=content, tag='ol', attr=attr, tag_type='double')

class Li(Elem):
	"""docstring for ."""
	def __init__(self, content=None, attr={}):
		"""
		__init__() method.

		Obviously.
		"""
		super().__init__(content=content, tag='li', attr=attr, tag_type='double')


class H1(Elem):
	"""docstring for ."""
	def __init__(self, content=None, attr={}):
		"""
		__init__() method.

		Obviously.
		"""
		super().__init__(content=content, tag='h1', attr=attr, tag_type='double')

class H2(Elem):
	"""docstring for ."""
	def __init__(self, content=None, attr={}):
		"""
		__init__() method.

		Obviously.
		"""
		super().__init__(content=content, tag='h2', attr=attr, tag_type='double')

class P(Elem):
	"""docstring for ."""
	def __init__(self, content=None, attr={}):
		"""
		__init__() method.

		Obviously.
		"""
		super().__init__(content=content, tag='p', attr=attr, tag_type='double')

class Div(Elem):
	"""docstring for ."""
	def __init__(self, content=None, attr={}):
		"""
		__init__() method.

		Obviously.
		"""
		super().__init__(content=content, tag='div', attr=attr, tag_type='double')


class Span(Elem):
	"""docstring for ."""
	def __init__(self, content=None, attr={}):
		"""
		__init__() method.

		Obviously.
		"""
		super().__init__(content=content, tag='span', attr=attr, tag_type='double')

class Hr(Elem):
	"""docstring for ."""
	def __init__(self, content=None, attr={}):
		"""
		__init__() method.

		Obviously.
		"""
		super().__init__(content=content, tag='hr', attr=attr, tag_type='simple')

class Br(Elem):
	"""docstring for ."""
	def __init__(self, content=None, attr={}):
		"""
		__init__() method.

		Obviously.
		"""
		super().__init__(content=content, tag='br', attr=attr, tag_type='simple')

if __name__ == '__main__':

	try:
		print(Html("test qui doit pas passer"))
	except Exception as e:
		print(e)
	print('-----------')
	elem_test = Html([Head([Meta(attr={'charset': 'utf-8'}), Title(Text('"Hello test"'))]),
				Body([H1(Text('"This is a test"')), Hr(),
				Br(),
				Span(Text('This is span')),
				Div(
					[Ul([Li(Text('This is a li in a ul'))])]),
				H2(Text('h2 maintenant')),
				P(Text('a p section\nla suite')),
				Table([Tr(Th(Text('This is a th in a table'))), Tr(Td(Text('this is a td')))]),
				Ol([Li(Text('<')), Li(Text('>')), Li(Text('"')) ]),
				Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})])])

	print(elem_test)
	print('-----------')
	elem = Html([Head(Title(Text('"Hello ground!"'))),
			Body([H1(Text('"Oh no, not again!"')),
			Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})])])
	print(elem)
