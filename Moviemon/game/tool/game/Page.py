from .elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul
from .elements import Ol, Li, H1, H2, P, Div, Span, Hr, Br
from .elem import Text

class Page:
	"""docstring for ."""
	def __init__(self, elem):
		self.i =0
		self.elem = elem
		self.__valide_instance__ = [Html, Head, Body, Title, Meta, Img, Table, Th,
		Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text]
		self.__valide_instance_body_div__ = [H1, H2, Div, Table, Ul, Ol, Span, Text]

	def __str__(self):
		s = ''
		if isinstance(self.elem, Html):
			s = '<!DOCTYPE html>\n'
		return s + str(self.elem)

	def __is_valide_instance__(self, noeud, instance):
		return (isinstance(noeud, instance))

	def __is_valide_html__(self, noeud):
		if len(noeud.content) != 2:
			return False
		if not isinstance(noeud.content[0], Head):
			return False
		if not isinstance(noeud.content[1], Body):
			return False
		return True

	def __is_valide_head__(self, noeud):
		if len(noeud.content) != 1:
			return False
		return isinstance(noeud.content[0], Title)

	def __is_valide_body_div__(self, noeud):
		if len(noeud.content) == 0:
			return True
		check = True
		for elem in noeud.content:
			if check == False:
				return False
			for instance in self.__valide_instance_body_div__:
				if self.__is_valide_instance__(elem, instance):
					check = True
					break;
				check = False
		return check

	def __is_valide_noeud_with_text(self, noeud):
		if len(noeud.content) == 0:
			return True
		if len(noeud.content) > 1:
			return False
		return isinstance(noeud.content[0], Text)

	def __is_valid_p__(self, noeud):
		if len(noeud.content) == 0:
			return True
		for elem in noeud.content:
			if not isinstance(elem, Text):
				return False
		return True

	def __is_valid_span__(self, noeud):
		if len(noeud.content) == 0:
			return True
		for elem in noeud.content:
			if not isinstance(elem, Text):
				if not isinstance(elem, P):
					return False
		return True

	def __is_valid_list__(self, noeud):
		if len(noeud.content) < 1:
			return False
		for elem in noeud.content:
			if not isinstance(elem, Li):
				return False
		return True

	def __is_valid_Tr__(self, noeud):
		if len(noeud.content) < 1:
			return False
		if isinstance(noeud.content[0], Th):
			for elem in noeud.content:
				if not isinstance(elem, Th):
					return False
			return True
		if isinstance(noeud.content[0], Td):
			for elem in noeud.content:
				if not isinstance(elem, Td):
					return False
			return True
		return False

	def __is_valid_table__(self, noeud):
		if len(noeud.content) == 0:
			return True
		for elem in noeud.content:
			if not isinstance(elem, Tr):
				return False
		return True


	def __is_valid_noeud__(self, noeud):
		for instance in self.__valide_instance__:
			if self.__is_valide_instance__(noeud, instance):
				if isinstance(noeud, Html):
					return self.__is_valide_html__(noeud)
				if isinstance(noeud, Head):
					return self.__is_valide_head__(noeud)
				if isinstance(noeud, Body):
					return self.__is_valide_body_div__(noeud)
				if isinstance(noeud, Div):
					return self.__is_valide_body_div__(noeud)
				if (isinstance(noeud, Title) or isinstance(noeud, H1) or isinstance(noeud, H2)
					or isinstance(noeud, Li) or isinstance(noeud, Th) or isinstance(noeud, Td)):
					return self.__is_valide_noeud_with_text(noeud)
				if isinstance(noeud, P):
					return self.__is_valid_p__(noeud)
				if isinstance(noeud, Span):
					return self.__is_valid_span__(noeud)
				if isinstance(noeud, Ul) or isinstance(noeud, Ol):
					return self.__is_valid_list__(noeud)
				if isinstance(noeud, Tr):
					return self.__is_valid_Tr__(noeud)
				if isinstance(noeud, Table):
					return self.__is_valid_table__(noeud)
				if isinstance(noeud, Text):
					return True
		return False

	def __loop_tree__(self, elem):

		if isinstance(elem, Text):
			return True
		if self.__is_valid_noeud__(elem) == False:
			return False

		for noeud in elem.content:
			if self.__loop_tree__(noeud) == False:
				return False
		return True

	def isvalid(self):
		return self.__loop_tree__(self.elem)

	def write_to_file(self, filename):
		fd = open(filename, 'w')
		fd.write(self.__str__())
		fd.close()

if __name__ == '__main__':
	elem_test_fail = Html([Head(Title(Text('"Hello test"'))),
				Body([H1(Text('"This is a test"')),
				Span(Text('This is span')),
				Div(
					[Ul([Li(Text('This is a li in a ul'))])]),
				H2(Text('h2 maintenant')),
				P(Text('a p section\nla suite')),
				Table([Tr(Th(Text('This is a th in a table'))), Tr(Td(Text('this is a td')))]),
				Ol([Li(Text('<')), Li(Text('>')), Li(Text('"')) ])
				])])
	elem_test = Html([Head(Title(Text('"Hello test"'))),
				Body([H1(Text('"This is a test"')),
				Span(Text('This is span')),
				Div(
					[Ul([Li(Text('This is a li in a ul'))])]),
				H2(Text('h2 maintenant')),
				Table([Tr(Th(Text('This is a th in a table'))), Tr(Td(Text('this is a td')))]),
				Ol([Li(Text('<')), Li(Text('>')), Li(Text('"')) ])
				])])

	elem = Html([Head(Title(Text('title'))), Body(Div(Span(Text('span') ) ) ) ] )

	p = Page(Html([Head(Title(Text('title'))), Body(Div(Span(Text('span') ) ) ) ] ))
	print(p)

	print('body simple', p.isvalid())


	p = Page(elem_test)
	p.write_to_file('test.html')


	print('body plus rempli', p.isvalid())

	p = Page(elem_test_fail)
	print('body with p', p.isvalid())
	print("test html")
	ph = Page(Html())
	print ('juste html:', ph.isvalid())
	phhb = Page(Html([Head(), Body()]))
	print('html [head, body]:', phhb.isvalid())
	phhb = Page(Html([Body(), Head()]))
	print('html [body, head]:', phhb.isvalid())
	print('test head')
	ph = Page(Head())
	print('head:', ph.isvalid())
	ph = Page(Head(Title()))
	print('head(Title):', ph.isvalid())
	ph = Page(Head([Title(), Div()]))
	print('head([Title, Div]):', ph.isvalid())
	print('test body')
	pb = Page(Body())
	print('body', pb.isvalid())
	pb = Page(Body(Div()))
	print('body(div)', pb.isvalid())
	pb = Page(Body([Div(), Div()]))
	print('body([div, div])', pb.isvalid())
	pb = Page(Body([Div(),Title(), Div()]))
	print('body([div,title div])', pb.isvalid())
	print('title, h1')

	pt = Page(Title(Text('ok')))
	print('title(Text(ok))', pt.isvalid())
	pt = Page(Title([Text('uo'), Text('yo')]))
	print('title([Text(uo), Text(yo)])', pt.isvalid())
	pt = Page(Title(Text('ok')))
	print('title(Text(ok))', pt.isvalid())

	pt = Page(H1([Text('uo'), Text('yo')]))
	print('h1([Text(uo), Text(yo)])', pt.isvalid())
	pt = Page(H1(Text('ok')))
	print('h1(Text(ok))', pt.isvalid())
	pt = Page(H1([Text('uo'), Text('yo')]))
	print('h1([Text(uo), Text(yo)])', pt.isvalid())

	print('p')
	p = Page(P(Text('yo')))
	print('p(text(yo))', p.isvalid())
	p = Page(P([Text('yo'), Text('yo')]))
	print('p([text(yo), text(yo)])', p.isvalid())
	p = Page(P([Text('yo'), Div(), Text('yo')]))
	print('p([text(yo), div(), text(yo)])', p.isvalid())

	print('span')
	p = Page(Span(Text('ok')))
	print('span(text(yo)', p.isvalid())
	p = Page(Span([Text('ok'), P(Text('lol'))]))
	print('span(text(yo), p(lol))', p.isvalid())
	p = Page(Span([Text('ok'), Div(), P(Text('lol'))]))
	print('span(text(yo),div, p(lol))', p.isvalid())

	print('ul ol')
	p = Page(Ul())
	print('Page(Ul())', p.isvalid())
	p = Page(Ul(Li()))
	print('Page(Ul(Li()))', p.isvalid())
	p = Page(Ol(Li()))
	print('Page(Ol(Li()))', p.isvalid())
	p = Page(Ol([Li(), Li()]))
	print('Page(Ol(Li(), Li()))', p.isvalid())

	p = Page(Ol([Li(),Div(),  Li()]))
	print('Page(Ol(Li(),Div(), Li()))', p.isvalid())

	p = Page(Tr())
	print('p = Page(Tr())', p.isvalid())

	p = Page(Tr(Td()))
	print('p = Page(Tr(Td))', p.isvalid())
	p = Page(Tr([Td(), Th()]))
	print('p = Page(Tr(Td, Th))', p.isvalid())


	p = Page(Table(Td()))
	print('p = Page(Table(Td))', p.isvalid())
	p = Page(Table([Tr(), Tr()]))
	print('p = Page(Table(Tr, Tr))', p.isvalid())
