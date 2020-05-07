
from typing import Any, Dict, Generic, List, TypeVar
import copy


T = TypeVar('T')
S = TypeVar('S')
U = TypeVar('U')


class MapTable(Generic[T, S, U]):
	

	def __init__(self, columns: List[T], rows: List[S], default_value: U):

		if columns is None:
			self.columns: Dict[T, int] = {}
		else:
			self.columns = {item: i for i,item in enumerate(columns)}

		if rows is None:
			self.rows: Dict[S, int] = {}
		else:
			self.rows = {item: i for i,item in enumerate(rows)}

		self.default_value: U = default_value
		self.data: List[List[U]] = [[default_value for j in range(len(self.columns))] for i in range(len(self.rows))]


	def get_item(self, col_key: T, row_key: S, restrict_bounds: bool = True) -> U:

		valid_col: bool = col_key in self.columns
		valid_row: bool = row_key in self.rows

		if (not valid_row) and (not valid_row) and restrict_bounds: # force 1 of the keys to be correct
			raise Exception('col_key and row_key are invalid')
		elif not valid_col:
			return self.default_value
		elif not valid_row:
			return self.default_value
		else:
			return self.data[self.rows[row_key]][self.columns[col_key]]


	def set_item(self, col_key: T, row_key: S, val: U) -> None:

		if not (col_key in self.columns and row_key in self.rows):
			raise Exception('invalid col_key or row_key')

		self.data[self.rows[row_key]][self.columns[col_key]] = val


	def get_row(self, row_key: S) -> List[U]:

		if row_key not in self.rows:
			raise Exception('invalid row_key')

		# return copy so that future modifications won't change the list
		return copy.copy(self.data[self.rows[row_key]])


	def get_col(self, col_key: T) -> List[U]:

		if col_key not in self.columns:
			raise Exception('invalid col_key')

		col_index: int = self.columns[col_key]

		return [row[col_index] for row in self.data]


	def __repr__(self) -> str:

		s: str = ''

		s += 'columns: {}\n'.format(list(self.columns.keys()))
		s += 'rows: {}\n'.format(list(self.rows.keys()))

		# I think this runs in O(n^2) time since strings are immutable, can this be made better?
		# for row in self.data:
		# 	s += str(row) + '\n' # todo: fix this, it adds an extra newline

		# not sure if the efficiency holds for python3 but see https://waymoot.org/home/python_string/
		# for why I did this
		s += '\n'.join([str(row) for row in self.data])

		return s
