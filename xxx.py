from statsmodels.tsa.arima_model import ARIMA


def choose_best_model(ts, max_surch, d=1):
    init_bic = float("inf")
    init_p = 1
    init_q = 0
    for p in range(1, max_surch):
        model = ARIMA(ts, order=(p, d, 0))
        try:
            results_ARMA = model.fit(disp=-1, method='css')
        except Exception as e:
            continue
        bic = results_ARMA.bic
        if bic < init_bic:
            init_p = p
            init_bic = bic

    return init_bic, init_p, init_q
    
