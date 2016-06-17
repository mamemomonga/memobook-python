## Pretty Print
PerlのData::Dumper, PHPのvar_dump的なもの

	data={ 'moge':'mogo' }
	import pprint
	pprint.PrettyPrinter(indent=4).pprint(data)

## ['aa','bb','cc'] を value="aa",value="bb",value="cc" にする

	values=['aa','bb','cc']
	result = ",".join( map( lambda n: 'value="%s"' % n, values ))
	print result

* [map](http://docs.python.jp/3/library/functions.html#map)
* [join](http://docs.python.jp/3/library/stdtypes.html#str.join)
* [lambda](http://docs.python.jp/3/reference/expressions.html#lambda)

