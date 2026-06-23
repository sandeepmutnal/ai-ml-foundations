# Project 12
# GUI Stock Market Prediction AI

import tkinter as tk
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = {
    "Open_Price": [100, 102, 101, 105, 107, 110, 108, 112, 115, 117],
    "High_Price": [105, 106, 104, 108, 111, 113, 112, 116, 118, 120],
    "Low_Price": [98, 100, 99, 103, 105, 108, 106, 110, 113, 115],
    "Volume": [1000, 1200, 1100, 1500, 1700, 1600, 1800, 1900, 2000, 2100],
    "Close_Price": [102, 101, 105, 107, 110, 108, 112, 115, 117, 119]
}

df = pd.DataFrame(data)

X = df[["Open_Price", "High_Price", "Low_Price", "Volume"]]
y = df["Close_Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)


def predict_price():
    try:
        open_price = float(entry_open.get())
        high_price = float(entry_high.get())
        low_price = float(entry_low.get())
        volume = float(entry_volume.get())

        prediction = model.predict([[open_price, high_price, low_price, volume]])

        result_label.config(
            text="Predicted Close Price: " + str(round(prediction[0], 2))
        )

    except:
        result_label.config(text="Please enter valid numbers")


window = tk.Tk()
window.title("Stock Price Prediction AI App")
window.geometry("400x350")

tk.Label(window, text="Open Price").pack()
entry_open = tk.Entry(window)
entry_open.pack()

tk.Label(window, text="High Price").pack()
entry_high = tk.Entry(window)
entry_high.pack()

tk.Label(window, text="Low Price").pack()
entry_low = tk.Entry(window)
entry_low.pack()

tk.Label(window, text="Volume").pack()
entry_volume = tk.Entry(window)
entry_volume.pack()

tk.Button(
    window,
    text="Predict Close Price",
    command=predict_price
).pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()