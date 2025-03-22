import marimo

__generated_with = "0.11.25"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def matrix_dot_vector():
    def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
        if len(a[0]) != len(b):
            return -1
    
        dot_vector = []
        for row in a:
            dot_product = 0
            for col in range(0, len(row)):
                dot_product += row[col] * b[col]
            dot_vector.append(dot_product)
    
        return dot_vector
    return (matrix_dot_vector,)


@app.cell
def _(matrix_dot_vector):
    matrix_dot_vector([[1, 2], [2, 4]], [1, 2])
    return


if __name__ == "__main__":
    app.run()
