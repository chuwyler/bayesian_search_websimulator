# Bayesian Search Websimulator

A very simple game that simulates Bayesian search. In contrast to brute force approaches, Bayesian search involves prior information and updating that prior after each individual search. The concept is well-explained by Jared S. Murray [here](https://jaredsmurray.github.io/sta371h/files/05_bayes_rule%20(2).pdf).

The app is based on flask, matplotlib and numpy. To run it, create a virtual environment with python==3.7.5 or similar and the requirements given in requirements.txt and then run `flask run` in the current directory. The app will then attach to a local port that you can access via web browser.

A running version can be found on [http://chuwyler.pythonanywhere.com](http://chuwyler.pythonanywhere.com).

This is just a simple demonstration that could profit from improvements on all ends! For questions and comments feel free to contact me via [cedric.huwyler@fhnw.ch](mailto:cedric.huwyler@fhnw.ch).

Some animations comparing how different search strategies change the probability distribution (code not included)

| Brute force   | Random        | Bayesian      |
| ------------- | ------------- | ------------- |
| ![](https://raw.githubusercontent.com/chuwyler/bayesian_search_websimulator/main/animations/animation_bruteforce_search.gif)      |![](https://raw.githubusercontent.com/chuwyler/bayesian_search_websimulator/main/animations/animation_random_search.gif) | ![](https://raw.githubusercontent.com/chuwyler/bayesian_search_websimulator/main/animations/animation_bayesian_search.gif) |



