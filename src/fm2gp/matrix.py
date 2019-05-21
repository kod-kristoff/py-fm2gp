import array


class Matrix:
    def __init__(self, n_rows, n_cols, data: list = None):
        if data:
            self.data = data
        else:
            self.data = [0 for r in range(n_rows)
                           for c in range(n_cols)]
        self.n_rows = n_rows
        self.__cols = n_cols - 1
        self.n_cols = n_cols
        self.__rows = n_rows - 1

        assert len(self.data) == self.n_rows * self.n_cols

    def mk_index(self, row, col):
        return row * self.n_cols + col

    def __getitem__(self, row_col):
        return self.data[self.mk_index(*row_col) ]

    def __setitem__(self, i_j, v):
        self.data[self.mk_index(*i_j)] = v

    def __add__(self, other):
        if (self.n_rows != other.n_rows
           or self.n_cols != other.n_cols):
               raise ValueError()

        assert len(self.data) == len(other.data)

        return Matrix(
                self.n_rows,
                self.n_cols,
                [s + o for s, o in zip(self.data, other.data)])

    def __mul__(self, other):
        if self.n_cols != other.n_rows:
            raise ValueError()

        m = Matrix(self.n_rows, other.n_cols)
        for r in range(m.n_rows):
            for c in range(m.n_cols):

                print(f'm = {m}, m.data = {m.data}')
                print(f'self.row({r}) = {self.row(r)}')
                print(f'other.col({c}) = {other.col(c)}')
                m[r, c] = sum(s*o for s, o in zip(self.row(r), other.col(c)))
                print(f'm[{r}, {c}] = {m[r,c]}')
                print(f'm = {m}')
        print(f'm = {m}')
        return m

    def __repr__(self):
        return f'Matrix({self.n_rows}, {self.n_cols}, {self.data})'

    def row(self, i):
        row_start = self.mk_index(i, 0)
        return self.data[row_start: row_start + self.n_cols]

    def col(self, j):
        return self.data[j::self.n_cols]

    def __eq__(self, other):
        return (self.n_rows == other.n_rows
                and self.n_cols == other.n_cols
                and self.data == other.data
                )

