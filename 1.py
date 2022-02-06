class QItem:
	def __init__(self, row, col, dist):
		self.starting_row = row
		self.starting_column = col
		self.dist = dist

	def __repr__(self):
		return f"QItem({self.starting_row}, {self.starting_column}, {self.dist})"

def minDistance(grid):
	source = QItem(0, 0, 0)


	source.starting_row = 0
	source.starting_column = 3
	target_row = 3
	target_col = 0

	visited = [[False for _ in range(len(grid[0]))]
			for _ in range(len(grid))]
	
	queue = []
	queue.append(source)
	visited[source.starting_row][source.starting_column] = True
	while len(queue) != 0:
		source = queue.pop(0)

		if ((source.starting_row == target_row) and (source.starting_column == target_col)):
			return source.dist

		#up
		if isValid(source.starting_row - 1, source.starting_column, grid, visited):
			queue.append(QItem(source.starting_row - 1, source.starting_column, source.dist + 1))
			visited[source.starting_row - 1][source.starting_column] = True

		#down
		if isValid(source.starting_row + 1, source.starting_column, grid, visited):
			queue.append(QItem(source.starting_row + 1, source.starting_column, source.dist + 1))
			visited[source.starting_row + 1][source.starting_column] = True

		#left
		if isValid(source.starting_row, source.starting_column - 1, grid, visited):
			queue.append(QItem(source.starting_row, source.starting_column - 1, source.dist + 1))
			visited[source.starting_row][source.starting_column - 1] = True

		#right
		if isValid(source.starting_row, source.starting_column + 1, grid, visited):
			queue.append(QItem(source.starting_row, source.starting_column + 1, source.dist + 1))
			visited[source.starting_row][source.starting_column + 1] = True

	return -1


def isValid(x, y, grid, visited):
	if ((x >= 0 and y >= 0) and
		(x < len(grid) and y < len(grid[0])) and
			(grid[x][y] != 0) and (visited[x][y] == False)):
		return True
	return False


if __name__ == '__main__':
	grid = [[0, 1, 0, 1],
			[1, 0, 1, 1],
			[0, 1, 1, 1],
			[1, 1, 1, 1]]

	print(minDistance(grid))
