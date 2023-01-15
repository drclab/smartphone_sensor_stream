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

parameters {
    /* ... declarations ... */
    vector[N] g1_betas; 
    vector[J] g2_betas;
    matrix[N, K] gammas; // group 1 factor
    matrix[J, K] deltas; // group 2 factors
}

transformed parameters {
    /* ... declarations ... statements ... */
    real linear_predictors[(N*J)];
    
}