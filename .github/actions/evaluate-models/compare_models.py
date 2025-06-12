import argparse
import tensorflow as tf
import numpy as np

def evaluate_model(model_path, x_test, y_test):
    model = tf.keras.models.load_model(model_path)
    _, accuracy = model.evaluate(x_test, y_test, verbose=0)
    return accuracy

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--new-model", required=True, help="Path to the new model artifact")
    parser.add_argument("--prod-model", required=True, help="Path to the production model artifact")
    args = parser.parse_args()

    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_test = x_test / 255.0 

    new_model_acc = evaluate_model(args.new_model, x_test, y_test)
    prod_model_acc = evaluate_model(args.prod_model, x_test, y_test)

    print(f"New model accuracy: {new_model_acc}")
    print(f"Production model accuracy: {prod_model_acc}")

    with open("result.txt", "w") as f:
        if new_model_acc > prod_model_acc:
            f.write("new")
            print("New model performs better.")
        else:
            f.write("old")
            print("Production model performs better.")