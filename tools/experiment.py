import numpy as np, json
g = np.random.default_rng(51)
x = np.c_[-1:1:12j]
y = np.sin(3 * x) + g.normal(0, .4, (12, 1))
X = np.c_[-1:1:99j]; Y = np.sin(3 * X)
one = lambda v: np.c_[v, v ** 0]
net = lambda v: np.tanh(one(v) @ A) @ B
W = g.normal(0, 5, (2, 64)); lr = .002
snaps = sorted(set(np.unique(np.round(np.logspace(0, np.log10(59999), 90)).astype(int)).tolist()))
out = {"x": x.ravel().round(4).tolist(), "y": y.ravel().round(4).tolist(), "snaps": snaps}
for p in 0, .5:
    A, B = W.copy(), np.zeros((64, 1))
    test, train, curves, masks = [], [], [], []
    for t in range(60000):
        a = np.tanh(one(x) @ A)
        m = (g.random(a.shape) >= p) / (1 - p)
        h = a * m; e = h @ B - y
        d = e @ B.T * m * (1 - a * a)
        A -= lr * one(x).T @ d; B -= lr * h.T @ e
        if t < 60 and p: masks.append("".join("1" if z > 0 else "0" for z in m[0]))
        if (t+1) % 100 == 0 or t == 0:
            test.append(round(float(np.mean((net(X) - Y) ** 2)), 5))
            train.append(round(float(np.mean((net(x) - y) ** 2)), 5))
        if t in snaps: curves.append(net(X).ravel().round(3).tolist())
    k = "plain" if p == 0 else "drop"
    out[k] = {"test": test, "train": train, "curves": curves, "B": B.ravel().round(4).tolist(), "A": A.round(4).tolist(),
              "trainFinal": round(float(np.mean((net(x) - y) ** 2)), 4)}
    if p: out["masks"] = masks
    print(k, out[k]["test"][-1], out[k]["test"][1], out[k]["trainFinal"], len(curves))
print("first mask, first 12 off:", out["masks"][0][:12].count("0"))
json.dump(out, open("data/dropout_run.json", "w"), separators=(",", ":"))
