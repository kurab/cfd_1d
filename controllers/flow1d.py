from models import condition, calculator
from views import output


def main():
    conditions = condition.LoadConditions()
    cond = conditions.cond
    outputter = output.OutputData()

    f = conditions.load_initial_shape()
    outputter.draw_figure(f)

    flow_calculator = calculator.FlowCalculation(cond['calc'], cond['flow'])
    time = 0.0
    tt = 0.0
    fd = [0] * cond['calc']['ni']
    while time <= cond['calc']['etime']:
        # f = flow_calculator.upwind_method(f)
        # f = flow_calculator.central_method(f)
        f, fd = flow_calculator.cip_method(f, fd)
        # outputter.draw_figure(f)
        if tt > 5.0:
            outputter.draw_figure(f)
            tt = 0.0
        time += cond['calc']['dt']
        tt += cond['calc']['dt']

    outputter.show_animation()
    # outputter.save_animation()
