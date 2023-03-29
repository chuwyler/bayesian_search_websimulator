import io
import random
from flask import Flask, Response, render_template, request, session, redirect, url_for
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from sim import SearchSimulator, show

app = Flask(__name__)
app.secret_key = b'_5#y2L"H3G8z\n\xec]/' # obviously changed in production webapp..

# initialize simulator
n_x = 5
n_y = 5
sim = SearchSimulator( n_x=n_x, n_y=n_y, p=0.6, exp=2.5 )

# login procedure - for the moment just for fun, username is not used for anything else than display
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('serve'))
    return '''
        <form method="post">
            Your nickname: <input type=text name=username>
            <input type=submit value="Start">
        </form>
    '''

# query the simulator and display results
@app.route('/game', methods=['GET', 'POST'])
def serve():
    global sim, max_tries

    q = request.form.get("q")    
    new_game = request.form.get("new_game")
    error_message = None
    
    # reset simulator if desired
    if new_game:
        print("new game!")
        sim = SearchSimulator( n_x=n_x, n_y=n_y, p=0.6, exp=2.5 )
    
    # if q is set, find out if it can be casted to integer
    if q is not None and not new_game:
        try:
            q_int = int(q)
        except:
            q_int = None
            error_message = "only numeric queries allowed"

        # find out if q_int is within the allowed values            
        if q_int is not None:
            if 0 <= q_int < n_x * n_y:
                found, n_tries = sim.query(int(q))
            else:
                error_message = "only numeric values between {} and {} allowed".format(0, n_x*n_y-1) 
        
    return render_template(
        'index.html', 
        username=session['username'],
        n_tries=sim.n_tries, 
        q=q, 
        queries=', '.join([str(i) for i in sim.queries]),
        found=sim.found, 
        true_sector=sim.true_sector,
        error_message=error_message
    )

# create the probability distribution map    
@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
    
def create_figure():
    fig = show( sim.prior, n_x=5, n_y=5, sector=sim.true_sector, found=sim.found )
    return fig

# return the flattened prior    
@app.route('/prior')
def return_prior():
    return ', '.join( [str(i) for i in sim.prior] )    


if __name__ == '__main__':
    app.run()

