data {
    /* ... declarations ... */
    int<lower=0> N; // number of group 1 observations
    int<lower=0> J; // number of group 2 observations
    int<lower=0> K; // numner of latent dimensions
    int X[(N*J), 2]; // covariate matrix
    vector[(N*J)] y;
    real<lower=0> beta_sigma;
    reak<lower=0> y_sigma;
}
