import jinja2
import json
import numpy as np
import matplotlib.pyplot as plt

import mpld3
from mpld3 import plugins, utils


class HighlightLines(plugins.PluginBase):
    """A plugin to highlight lines on hover"""

    JAVASCRIPT = """
    mpld3.register_plugin("linehighlight", LineHighlightPlugin);
    LineHighlightPlugin.prototype = Object.create(mpld3.Plugin.prototype);
    LineHighlightPlugin.prototype.constructor = LineHighlightPlugin;
    LineHighlightPlugin.prototype.requiredProps = ["line_ids"];
    LineHighlightPlugin.prototype.defaultProps = {alpha_bg:0.3, alpha_fg:1.0}
    function LineHighlightPlugin(fig, props){
        mpld3.Plugin.call(this, fig, props);
    };

    LineHighlightPlugin.prototype.draw = function(){
      for(var i=0; i<this.props.line_ids.length; i++){
         var obj = mpld3.get_element(this.props.line_ids[i], this.fig),
             alpha_fg = this.props.alpha_fg;
             alpha_bg = this.props.alpha_bg;
         obj.elements()
             .on("mouseover", function(d, i){
                            d3.select(this).transition().duration(50)
                              .style("stroke-opacity", alpha_fg); })
             .on("mouseout", function(d, i){
                            d3.select(this).transition().duration(200)
                              .style("stroke-opacity", alpha_bg); });
      }
    };
    """

    def __init__(self, lines):
        self.lines = lines
        self.dict_ = {"type": "linehighlight",
                      "line_ids": [utils.get_id(line) for line in lines],
                      "alpha_bg": lines[0].get_alpha(),
                      "alpha_fg": 1.0}


# Parameters
N_paths = 400
N_steps = 400

# 100 evenly-spaced values from 0 to 10
x = np.linspace(0, N_steps, N_steps)

# Generate matrix of -1's and 1's, then take their cumulative sum
y = 2* np.floor(2 * (np.random.random((N_paths, N_steps)) )) -1
y = np.cumsum(y, axis=1)

# Calculate the average distance from zero
avg = np.mean(np.absolute(y), axis=0)
ysqrt = np.sqrt(2*x/3.14159265)


# Plotting Jazz
fig, ax = plt.subplots(subplot_kw={'xticks': [], 'yticks': []})
lines = ax.plot(x, y.transpose(), color='blue', lw=1, alpha=0.1)
avgPlot = plt.plot(x, avg, color='red', lw=2, alpha=1)
sqrtPlot = plt.plot(x, ysqrt, color='green', lw=2, alpha=1)

plugins.connect(fig, HighlightLines(lines))
mpld3.save_html(fig, "testfigd3.html")

