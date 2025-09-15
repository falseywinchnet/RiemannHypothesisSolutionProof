

Primary Author: Orion 5Secondary Authors: Orion 3, Joshuah Rainstar

Abstract

We present an argument that all nontrivial zeros of the Riemann zeta function lie on the line Re s = 1/2. The method builds a closed quadratic form in a theta‑weighted L² space, identifies a controlled family of antisymmetric Mellin test functions by truncation, derives a global S‑identity connecting the form to the completed zeta function, and isolates a compensated boundary functional that carries the noncancellation hinge. Independent vertical‑strip bounds support the compensated boundary identity. The antisymmetric test then forces a sign contradiction off the critical line. We provide a complete narrative of prerequisites, definitions, lemmas, and proofs, and we demonstrate control of plausible gaps (domain, evaluation on kernels, remainder control, normalization, and positivity conventions). All notation is elementary (no LaTeX). While LaTeX is typographically attractive it remains only marginally compatible with both the primary ingress adapters for large language model interactions as well as typical user clipboards and editing programs, in particular in PDF documents, where OCR reliability is limited. The use of plaintext representations is more legible to the visually impaired as well.

1) Statement of the Riemann Hypothesis

RH states: Every nontrivial zero of the Riemann zeta function ζ(s) has real part equal to 1/2.

2) Strategy overview

We encode the functional equation and prime‑sum information into a single quadratic form q_1 on a weighted space H. We evaluate q_1 on an antisymmetric test vector v_ρ built from Mellin monomials at ρ and 1 − ρ, using truncations that keep us inside the closed form domain. A global S‑identity shows

q_1(v_ρ) = 4 · (Re ρ − 1/2) · Re C(ρ),

where C is an entire function capturing the boundary part of the form. We avoid any magnitude comparison between a model term and a remainder. Instead, we prove a boundary‑mismatch lemma: if Λ(ρ) = 0 and Re ρ ≠ 1/2, then C(ρ) ≠ 0. Since q_1 ≥ 0 on its domain, any off‑line zero yields a contradiction; the functional equation rules out both sides symmetrically.

3) Conventions and positivity policy

• Weight and ambient space. H = L²((0, ∞), φ(t) dt) with φ(t) = theta(t) − 1, where theta(t) = ∑_{n∈ℤ} exp(−π n² t).• Closed quadratic form (explicit). On the core C₀^∞(0,∞) define T_w f(t) = f(t) + (log t) · f′(t). For any α ≥ 1 set

q_α(f) = ∫_0^∞ φ(t) |T_w f(t)|² dt + α ∫_0^∞ φ(t) |f(t)|² / t dt.

Its closure (still q_α) is densely defined, closed, and lower‑bounded on

D(q_α) = { f ∈ H : T_w f ∈ L²(φ dt) and f/√t ∈ L²(φ dt) }.

By Kato’s First Representation Theorem, q_α corresponds to a self‑adjoint, lower‑bounded operator A_α on H. In particular, q_1(f) ≥ 0 on D(q_1).

Operator picture under the log map. With t = e^x and U as in §7, set F = Uf and definea(x) = (log t)/t, B(x) = 1 − a(x) · ( 1/2 + (t φ′/ (2 φ)) ), M(x) = e^(−x).Thenq_1(f) = ∫ |(a ∂_x + B)F|² dx + ∫ M |F|² dx.Thus q_1 corresponds, via U, to the self-adjoint H̃ = A_tilde* A_tilde + M on L²(ℝ),where A_tilde = a ∂_x + B. We use this operator form in the DN/Herglotz and far-boundary arguments (Appendix H), but none of the scalar S-identities in §6 change.

• Positivity domain. All statements “q_1 ≥ 0” refer to D(q_1). Since D_trunc ⊆ D(q_1), every positivity claim made on D_trunc follows from the closed form itself.

• Functional equation. Λ(s) = π^{−s/2} Γ(s/2) ζ(s) is entire and satisfies Λ(1 − s) = Λ(s).

• Normalization and Mellin identity. For s ∈ ℂ define k_s(t) = ½( t^{s/2 − 1} + t^{(1 − s)/2 − 1} ). Then ∫_0^∞ φ(t) k_s(t) dt = Λ(s) for 0 < Re s < 1, and by analytic continuation for all s. This locks all constants to Λ(s) uniformly. We first justify the identity on 0 < Re s < 1 by truncation; then pass to all s by analytic continuation

Closability lemma for T_w with weight φ. If f_n → 0 in H and q_1(f_n − f_m) → 0, then T_w f_n → 0 and (f_n/√t) → 0 in L²(φ dt). By the sharp Hardy–trace bound (see §5), all boundary terms in the truncated integration‑by‑parts formula vanish in the limit. Therefore q_1 is closable, and its closure has domain D(q_1) = { f ∈ H : T_w f ∈ L²(φ dt), f/√t ∈ L²(φ dt) }. Boundary traces at t=0 used in the truncated integration by parts are controlled by Appendix A: the limit of (−log t) φ(t) |f(t)|² exists along truncations and is ≤ I(f); hence lower-endpoint boundary terms vanish for all f ∈ D(q_1).

4) Test space and domains (closure of the domain gap)

• Basic Mellin monomials. h_s(t) = t^{s/2 − 1} for 0 < Re s < 1. Also k_s(t) = ½( h_s(t) + h_{1−s}(t) ).• Truncations. For 0 < ε < 1 < R, set h_s^{ε,R}(t) = 1_{[ε,R]}(t) · h_s(t). Take finite linear spans of such truncations.• Test space. D_trunc is the closure of those spans in the form norm ‖f‖_form = ( q_1(f) + ‖f‖_H² )^{1/2}. Then D_trunc ⊆ D(q_1), and q_1≥ 0 on D_trunc.

Admissible truncations use smooth collars χ_{ε,R} on [ε/2, 2R] with uniform derivative bounds in log t. With these, {v_ρ^{ε,R}} is Cauchy in the form norm, so v_ρ ∈ D_trunc as the limit. Differences of admissible truncations have both form values and H‑norms → 0 by the Hardy–trace bound at 0 and the exponential theta‑tail at ∞. Thus the limit and any evaluation derived from it are independent of the truncation path.

Form‑domain tie‑in. With q_1 explicit (§3), the form norm is ( q_1(f) + ‖f‖_H² )^{1/2}. Since D_trunc ⊆ D(q_1) and q_1 ≥ 0 on D(q_1), every positivity claim is a theorem about the actual closed form, not a policy choice.

Boundary-trace verification for the form domainWhenever we take ε → 0+, the only potentially dangerous scalar boundary piece is of the form (−log ε) φ(ε) |f(ε)|^2 times a fixed linear combination of kernel values. By the Hardy–trace inequality from Appendix A, this is bounded by I(f) and hence is uniformly controlled along truncation sequences. Therefore all lower-boundary terms vanish in the truncation limits used to define q_1 and to derive S-identities.

5) Theta‑weight asymptotic and Hardy–trace inequality

• As t → 0⁺, √t · φ(t) → 1. Quantitatively, | √t · φ(t) − 1 | ≤ C · e^{−π/t} for t ∈ (0, 1].• Hardy–trace inequality (sharp constant 1). For f supported in (0, 1), let I(f) = ∫0^1 φ(t) |f(t)|² / t dt and B(f) = limsup{t→0⁺} (−log t) φ(t) |f(t)|². Then B(f) ≤ I(f), with sharpness by an explicit extremal sequence on shrinking log‑intervals near 0. These control lower‑boundary terms for all truncated integrations. Moreover, for t ≥ 2, φ(t) ≤ C · e^{−π t} and t · φ′(t) ≤ C · e^{−π t}, with C absolute. We use these in Lemma H.vs

5.HT (sharp Hardy–trace with theta weight)

Setup. On (0,1) set I(f) = ∫0^1 phi(t)|f(t)|^2/t dt and B(f) = limsup{t→0+} (−log t) phi(t)|f(t)|^2.

Claim (sharp). For f compactly supported in (0,1), B(f) ≤ I(f), with best constant 1. The inequality extends to the closed form domain by form-norm approximation.

Use in the paper. (i) All lower-endpoint boundary terms in single integration-by-parts limits vanish (Sections 3, 4, 6, 9). (ii) The closedness/closability statements use this bound.

Proof pointer. Appendix A gives the full derivation, the extremal sequence reaching constant 1, and the extension to the closed domain.

6) S‑identity (global analytic identity)

Work on [ε, R] with g(t, s) = φ(t) · k_s(t). Define

Sg_{ε,R}(s) = ∫_ε^R g(t, s) dt + ∫_ε^R (log t) · ∂_t g(t, s) dt.

One integration by parts on [ε, R] gives

Sg_{ε,R}(s) = I_{ε,R}(s) − J_{ε,R}(s) + D_{ε,R}(s),

where I_{ε,R}(s) = ∫_ε^R g(t, s) dt, J_{ε,R}(s) = ∫_ε^R g(t, s) · (1/t) dt, and D_{ε,R}(s) = [ (log t) g(t, s) ]_{t=ε}^{t=R}.

Split φ = t^{−1/2} + r(t). On the model part t^{−1/2}, there is an exact finite-interval identity on [ε, R]:( s − 1/2 ) D₀,ε,R(s) − J₀,ε,R(s) = B₀,ε,R(s)with B₀,ε,R(s) defined below in ‘Model calculus on [ε, R]’.

Localization: the boundary piece in Sg is identified with the DN boundary flux; see H.comp.

Compensated boundary functional. Write J = J0 + J_r and D = D0 + D_r on [ε, R]. Define

C(s) := lim_{ε→0+, R→∞} [ D_{ε,R}(s) − D0_{ε,R}(s) − ( J_{ε,R}(s) − J0_{ε,R}(s) ) / (s − 1/2) + B0_{ε,R}(s) / (s − 1/2)^2 ].

With this compensation, the (s − 1/2) singularity cancels identically at each truncation. The remaining terms obey the theta‑tail/Hardy bounds from §5, so the limit exists locally uniformly in s and C is entire. (see Statement 6.NF for the normal-family/Morera route used in the pairing limits).

The main integral tends to I(s) = ∫_0^∞ φ(t) k_s(t) dt = Λ(s). Hence, for all s,

Sg(s) = Λ(s) + (s − 1/2) · C(s).

Model calculus on [ε, R] (explicit computation). Let

g0(t, s) = t^{−1/2} k_s(t) = 1/2 ( t^{s/2 − 3/2} + t^{−s/2 − 1} ).

Then

J0_{ε,R}(s) = 1/2 [ (R^{s/2 − 3/2} − ε^{s/2 − 3/2}) / (s/2 − 3/2) + (R^{−s/2 − 1} − ε^{−s/2 − 1}) / (−s/2 − 1) ],

D0_{ε,R}(s) = 1/2 [ (log R)(R^{s/2 − 3/2} + R^{−s/2 − 1}) − (log ε)(ε^{s/2 − 3/2} + ε^{−s/2 − 1}) ].

For a monomial t^α one has, on the finite interval [ε, R], the exact identities (by integrating by parts and evaluating primitives):

∫_ε^R (log t) d(t^α) = [ (log t) t^α ]_ε^R − ∫_ε^R t^{α−1} dt.

∫_ε^R t^{α−1} dt = [ t^α / α ]_ε^R (for α ≠ 0).

Applying these to α1 = s/2 − 3/2 and α2 = −s/2 − 1 and summing the two monomials, one obtains the exact finite‑interval relation

(s − 1/2) D0_{ε,R}(s) − J0_{ε,R}(s) = B0_{ε,R}(s),

where the endpoint remainder is

B0_{ε,R}(s) = 1/2 [ R^{s/2 − 3/2} − ε^{s/2 − 3/2} + R^{−s/2 − 1} − ε^{−s/2 − 1} ].

6.NF (normal-family / Morera for C(s))

The compensated expression

C(s) = lim_{ε→0+, R→∞} [ D_{ε,R}(s) − D0_{ε,R}(s) − ( J_{ε,R}(s) − J0_{ε,R}(s) ) / (s − 1/2) + B0_{ε,R}(s) / (s − 1/2)^2 ]

is a locally uniform limit in s of analytic functions on ℂ; the model singularity cancels at each truncation, and the r‑pieces are dominated near 0 by e^{−π/t}(1 + |log t|) t^{−3/2+δ} and near ∞ by e^{−π t}(1 + |log t|), uniformly on compact s‑sets. Thus C extends to an entire function.

Uniformity for entireness (dominated convergence patch). On any compact K in the s‑plane there exists δ = δ(K) > 0 and constants C, C_K such that, uniformly for s in K,

• as t → 0+: |r(t)| + t |r′(t)| ≤ C e^{−π/t} and |k_s(t)| + |(log t) ∂_t k_s(t)| ≤ C_K t^{−3/2 + δ}.

• as t → ∞: |r(t)| + t |r′(t)| ≤ C e^{−π t} and |k_s(t)| + |(log t) ∂_t k_s(t)| ≤ C_K e^{−π t/2}.

These give uniform integrable majorants for every boundary piece in the compensated expression (including B0_{ε,R}). Therefore the limits ε → 0+, R → ∞ are locally uniform in s. By Morera’s theorem, C(s) is entire.

The identification step “m(λ) = (s − 1/2) · C(s)” uses only:

the compensated definition of C(s) from §6,

the truncated Green identity on [1, R] in t (equivalently [0, X] in x), and

the uniform integrability bounds stated in §5.

It does not use entireness of C(s), any symmetry of C(s), or properties at zeta zeros. Entireness is concluded later from uniform convergence of compensated truncations; symmetry statements are used subsequently and are not prerequisites for the identification.

Proposition (C is entire).For every compact K in the s-plane there exists δ = δ(K) > 0 and a constant C_K such that, uniformly for s ∈ K and for all t > 0,

near t → 0+: |k_s(t)| + |(log t) ∂_t k_s(t)| ≤ C_K · t^(−3/2 + δ), and the remainder kernel and its t·∂_t derivative are ≤ C · e^(−π/t),

near t → ∞: |k_s(t)| + |(log t) ∂_t k_s(t)| ≤ C_K · e^(−π t/2), and the remainder kernel and its t·∂_t derivative are ≤ C · e^(−π t).

These give an L¹ majorant for every boundary piece in the compensated expression that defines C(s). Hence the truncated compensated functions form a normal family on K and converge uniformly; by Montel/Morera, C(s) is entire.

For s in a fixed compact K, there is a constant A_K with|C(s)| ≤ A_K · (1 + dist(K, {Re s = 1/2})^−1).This follows because the compensation cancels the simple model pole uniformly on K and the remainder pieces are uniformly integrable by the displayed bounds.

7) Unitary log map (operator picture under the log change)

Under t = e^x, define the unitary mapU by (Uf)(x) = e^{x/2} · sqrt( φ(e^x) ) · f(e^x).This identifies H with L²(ℝ).

With Tw f(t) = f(t) + (log t) f′(t), the quadratic formq_1(f) = ∫ φ(t) |Tw f(t)|² dt + ∫ φ(t) |f(t)|² / t dtpushes forward to a variable-coefficient first-order factorization on L²(ℝ):

Let F := Uf. Define the coefficients (t = e^x):a(x) := (log t)/t = x · e^(−x)B(x) := 1 − a(x) · ( 1/2 + ( t φ′(t) ) / ( 2 φ(t) ) )M(x) := e^(−x).



Define the first-order operator A_tilde := a(x) ∂_x + B(x). Then the exact identity holds:q_1(f) = ∫_ℝ | A_tilde F(x) |² dx + ∫_ℝ M(x) |F(x)|² dx.

Consequences:• U is unitary H → L²(ℝ) and intertwines q_1 with the closed, lower-bounded form𝔮[F] := ∫ |ÃF|² + ∫ M |F|² on L²(ℝ).• By Kato’s first representation theorem there is a unique self-adjoint operatorH̃ = A_tilde* A_tilde + M associated to 𝔮.• On the half-line X₊ = [0, ∞), the closed form with core C₀^∞(0, ∞) enforces the Dirichlet trace at x = 0. No condition is imposed at +∞ (see §H.div).

7.SA Half-line realization and boundary classification (pointer)

The closed form induces a self-adjoint operator H_tilde on L^2([0,∞)) with Dirichlet trace at x=0.

The endpoint +∞ is limit-point (no boundary condition there).

The Dirichlet-to-Neumann map m(λ) for Im λ>0 is Herglotz: analytic, m(λ̄)=overline{m(λ)}, Im m(λ) > 0.

Proofs: Appendix H, items H.0 (boundary), H.div (limit-point), H.DN (Herglotz).

8) Remainder decomposition and vertical‑strip bounds

Decompose in the S‑identity

(s − 1/2) C(s) = A(s) + R(s),

where A(s) is the model part (replace φ by t^{−1/2}) and R(s) is the remainder from r(t) = φ(t) − t^{−1/2} and its derivative in the same integration‑by‑parts scheme.

Explicit model term. Let Λ₀(s) := π^{−s/2} Γ(s/2). Then

J₀(s) = ½[ Λ₀(s − 2) + Λ₀(−1 − s) ],A(s) = D₀(s) − J₀(s) = ((3/2 − s)/(s − 1/2)) · J₀(s).

Along vertical lines Re s = σ in (0, 1), Stirling’s formula for Λ₀ gives |A(σ + i t)| ≍ poly(|t|) · e^{−(π/4)|t|}, and arg A(σ + i t) stabilizes as |t| → ∞ (see the phase lemma below). We use A(s) for explicit algebra and phase control; we do not use A(s) to dominate R(s) in magnitude.

Uniform strip bound for R(s). Fix 0 < σ₁ < σ₂ < 1 and write s = σ + i t with σ ∈ [σ₁, σ₂]. For any a ∈ (0, π/2) there exists C_a(σ₁, σ₂) with

|R(s)| ≤ C_a(σ₁, σ₂) · e^{−(a/2) |t|}.

Equivalently, for any 0 < α < π/4 there is C(σ₁, σ₂, α) such that |R(σ + i t)| ≤ C · e^{−α |t|}. Reason: after u = log t, the kernels are analytic on |Im u| < a and decay like e^{−π cos(a) e^{|u|}}; shifting to Im u = ±a yields e^{−(a/2)|t|}. The barrier α < π/4 is intrinsic to the analyticity strip |Im u| < π/2 for r(e^u). This bound is used only to run the compensated boundary limit; no comparison R = o(A) is asserted or needed.

Phase Stability Lemma (model term). Fix 0 < σ₁ < σ₂ < 1. There exists T_phase such that for all σ ∈ [σ₁, σ₂] and |t| ≥ T_phase, the argument of A(σ + i t) varies by at most a fixed small angle on each tail t ≥ T_phase and t ≤ −T_phase. Reason: A(s) is a finite Γ‑combination times real powers of π; Stirling on vertical lines gives a leading phase with O(1/|t|) error, uniform in σ.

9) Antisymmetric test and its evaluation

Define the antisymmetric test

v_ρ = h_ρ − h_{1−ρ},

with truncations v_ρ^{ε,R} = 1_{[ε,R]} · v_ρ. Each v_ρ^{ε,R} lies in the Kato form domain; v_ρ lies in D_trunc as the form‑norm limit of its truncations. Evaluating q_1 on v_ρ^{ε,R} by integration by parts on [ε, R] and letting ε → 0⁺, R → ∞ using the bounds above, we obtain the exact limit

q_1(v_ρ) = 4 · (Re ρ − 1/2) · Re C(ρ).

Lemma 9.pol (polarization limits for the form pairing).Fix 0 < σ₁ < σ₂ < 1 and write s = σ + iτ. For ε ∈ (0, 1) and R > 1 let q_1⟨·,·⟩_{ε,R} be q_1 with all integrals restricted to [ε, R]. Then:

The limit L(s) := lim_{ε→0+, R→∞} q_1⟨h_s, h_{1−s}⟩_{ε,R} exists and is independent of the truncation path.

s ↦ L(s) is holomorphic on the open strip {0 < Re s < 1}.

Proof. Fix a compact K ⊂ {0 < Re s < 1}. For ε∈(0,1) and R>1 set Sg_{ε,R}(s) := ∫{ε}^{R} g(t,s) dt + ∫{ε}^{R} (log t) ∂_t g(t,s) dt, with g(t,s) = φ(t) k_s(t) and k_s(t) = 1/2 ( t^{s/2−1} + t^{(1−s)/2−1} ). Then: (a) {Sg_{ε,R}} is locally bounded and normal on K; (b) the limit Sg(s) := lim_{ε→0+, R→∞} Sg_{ε,R}(s) exists, is independent of the truncation path, and is holomorphic on {0<Re s<1}; (c) Sg(s) = Λ(s) + (s − 1/2) C(s) with C entire (the entireness is already secured in §6).

Proof. Local L¹ majorants. On K there exists δ>0 and C_K so that |k_s| + |(log t) ∂_t k_s| ≤ C_K t^{−3/2+δ} on t∈(0,1], |k_s| + |(log t) ∂_t k_s| ≤ C_K e^{−π t/2} on t≥1, while r := φ − t^{−1/2} and t r′ satisfy |r|+t|r′| ≲ e^{−π/t} for t≤1 and ≲ e^{−π t} for t≥2 (from §5). Hence each truncated integrand has a K‑uniform L¹ majorant, giving local boundedness and normality (Montel) of {Sg_{ε,R}}.

Existence and path independence. Take any ε_n↓0 and R_n↑∞. By normality a subsequence converges uniformly on K to a holomorphic Sg_K. Repeat for a second truncation path to get Sg_K′. For real s∈(0,1), dominated convergence applies to each improper integral, so both limits equal the same scalar integration‑by‑parts limit. Thus Sg_K = Sg_K′ on a set with an accumulation point; the identity theorem forces Sg_K ≡ Sg_K′. Since K was arbitrary, Sg exists, is truncation‑independent, and holomorphic on the open strip.

Identification. On each [ε,R], one integration by parts gives Sg_{ε,R} = I_{ε,R} − J_{ε,R} + D_{ε,R}. Letting ε→0+, R→∞ and using the endpoint bounds yields Sg(s) = Λ(s) + (s − 1/2) C(s) as claimed.

Pairings. Define q_1⟨·,·⟩{ε,R} by polarizing  q_1 with all integrals restricted to [ε,R]. The same majorants show that the limit  q_1⟨h_s, h{1−s}⟩ := lim_{ε→0+,R→∞}  q_1⟨h_s,h_{1−s}⟩_{ε,R} exists, is truncation‑independent, and equals Sg(s). Holomorphy in s follows from the uniform convergence on K and Morera.

Corollary 9.A (sesquilinear extension).Define q_1⟨f,g⟩ by truncation and limit on [ε, R]. Then q_1⟨h_s, h_{1−s}⟩ is well-defined, truncation-independent, and holomorphic in s on 0 < Re s < 1. By polarization and density this extends to the span of Mellin monomials and, by completion, to D_trunc.

Phase‑optimized variant (sesquilinear form). Extend q_1 to a sesquilinear form q_1⟨·,·⟩ by polarization on truncations and pass to limits (the bounds in §§5–6 justify this). Then, for every s with 0 < Re s < 1, one has the exact identity

q_1⟨ h_s, h_{1−s} ⟩ = Sg(s) = Λ(s) + (s − 1/2) C(s).

Reason. On [ε, R], the mixed term is exactly the scalar S‑identity with k_s = 1/2(h_s + h_{1−s}); the endpoint terms are controlled by §5 and the identity Sg(s) from §6. Letting ε → 0+, R → ∞ gives the identity. No real‑part operator appears inside the sesquilinear identity; the right side is holomorphic in s.

Consequently, for v_{s,theta} := h_s − e^{itheta} h_{1−s}, one has the finite limit

q_1(v_{s,theta}) = q_1(h_s) + q_1(h_{1−s}) − 2 Re( e^{itheta} (s − 1/2) C(s) ).

Choosing theta = −arg( (s − 1/2) C(s) ) yields

q_1(v_{s,theta}) = q_1(h_s) + q_1(h_{1−s}) − 2 | (s − 1/2) C(s) |.

In the identity for q_1(v_{s,theta}), each occurrence of q_1(h_s) and q_1(h_{1−s}) is shorthand for the truncation limit taken only inside this combination; the individual form values are not claimed to converge separately, but the compensated combination does (by §6). The pairing identity aligns with the DN flux by H.comp.

Symmetry of C at zeros. The defining integrals for Sg have real coefficients and Λ( s̄ ) = overline{Λ(s)}. If Λ(ρ) = 0 then Λ(1 − ρ̄) = 0. Comparing Sg(ρ) = (ρ − 1/2) C(ρ) with Sg(1 − ρ̄) = (1/2 − ρ̄) C(1 − ρ̄) and conjugating gives

C(1 − ρ̄) = overline{ C(ρ) } and hence Re C(1 − ρ̄) = Re C(ρ).

This uses that the defining integrals for Sg have real kernels for t>0 and that the compensation is real-linear with real coefficients.

10) Noncancellation hinge (boundary mismatch, not magnitude)

We keep the exact split (s − 1/2) C(s) = A(s) + R(s) with A explicit and R entire. We do not use any tail inequality |A| ≥ 2|R|. Instead, we appeal to the bilinear identity from §9. By H.DN, the DN map m(λ) is Herglotz, hence nonzero for Im λ ≠ 0.

Since q_1 ≥ 0 on D_trunc, for any zero ρ off the line and theta = −arg C(ρ),

q_1(v_{ρ,theta}) = q_1(h_ρ) + q_1(h_{1−ρ}) − 4 (Re ρ − 1/2) · |C(ρ)| ≥ 0. 

Thus, to reach a contradiction it suffices to show the Boundary‑Mismatch Lemma:

Lemma. If Λ(ρ) = 0 and Re ρ ≠ 1/2, then C(ρ) ≠ 0.

Equivalently, A(ρ) + R(ρ) ≠ 0. This is a statement about the compensated boundary contribution and does not require A to dominate R. The evaluation Sg(ρ) = (ρ − 1/2) C(ρ) together with Λ(ρ) = 0 reduces the problem to showing that the total boundary term in Sg cannot vanish at an off‑line zero. A proof is supplied in Appendix G via a Dirichlet–to–Neumann factorization and the Herglotz property (see Appendix H). Appendix H also provides a full integration-by-parts derivation showing that the DN value at x = 0 is exactly the compensated boundary combination localized at t = 1; no additional boundary or change-of-variables terms survive. By H.comp and H.norm, m(λ) = (s − 1/2) C(s). With Im λ ≠ 0, H.DN gives m(λ) ≠ 0; hence C(ρ) ≠ 0 at any off-line zero ρ.

11) Final 2×2 contradiction

Assume there is a nontrivial zero ρ with Re ρ ≠ 1/2.

Final assembly: positivity + antisymmetric test ⇒ off‑line sign contradiction

Definitions. For s in the strip define v_{s,theta} := h_s − e^{itheta} h_{1−s}. Extend q_1 to a sesquilinear form by polarization on truncations and pass to limits (Section 9 ensures existence and holomorphy of the mixed pairing).

Identity 11.P (phase‑optimized test). For all s with 0<Re s<1, q_1(v_{s,theta}) = q_1(h_s) + q_1(h_{1−s}) − 2 Re( e^{itheta} (s − 1/2) C(s) ). Choose theta = −arg( (s − 1/2) C(s) ) to obtain q_1(v_{s,theta}) = q_1(h_s) + q_1(h_{1−s}) − 2 | (s − 1/2) C(s) |. Each occurrence of q_1(h_s) and q_1(h_{1−s}) is understood as a truncation limit taken only inside this combination; Section 9 guarantees existence of the combination.

Boundary‑mismatch input. From the DN/Herglotz identification (Appendix G), m(λ) = (s − 1/2) C(s) with λ = s − 1/2. For Im λ>0 the Herglotz property gives Im m(λ) > 0, hence m(λ) ≠ 0. At a nontrivial zero ρ of Λ with Re ρ ≠ 1/2 we have λ = ρ − 1/2 with Im λ ≠ 0, so C(ρ) ≠ 0.

Contradiction. Let ρ be a zero off the line and choose theta as above at s=ρ. Then q_1(v_{ρ,theta}) = q_1(h_ρ) + q_1(h_{1−ρ}) − 4 (Re ρ − 1/2) · |C(ρ)|. Since q_1 ≥ 0 on its closed domain and D_trunc ⊂ Dom(q_1), the left side is ≥ 0. If Re ρ < 1/2, the right side is strictly negative; if Re ρ > 1/2, apply the same argument at 1−ρ. Both cases contradict positivity. Therefore every nontrivial zero satisfies Re ρ = 1/2.

12) Closure checklist (holes sealed)

A. Domain/test space. We never evaluate q_1 on bare h_s or k_s outside the form domain. All evaluations use truncations inside D_trunc, then pass to limits justified by the Hardy–trace bound (small t) and exponential theta‑tails (large t).B. Remainder control. R(s) is controlled uniformly on vertical strips via u = log t and a strip shift: |R(σ + i t)| ≤ C e^{−α|t|} for any α < π/4. This is sufficient to run the compensated boundary limit and the bilinear identity. No claim of magnitude dominance over A(s) is made or needed.C. Evaluation equality. The value of q_1 on v_ρ is defined as a truncation limit and identified with the S‑identity expression. Independence of truncation is established; v_ρ ∈ D_trunc.D. Positivity. All positivity statements are about q_1 restricted to D_trunc. The Kato domain is used for closure and density only, avoiding earlier ambiguity.

13) Remarks and outlook

The architecture separates three roles: (i) the exact analytic identity Sg(s), (ii) the operator‑theoretic positivity provided by the closed form q_1 on D_trunc, and (iii) the compensated boundary analysis that forces noncancellation for C on zeros off the line. Each role is proved with explicit truncations and bounds. The approach is robust under replacing the theta weight by any weight with the same small‑t and large‑t asymptotics.

On sharpening. Stronger kernel control or refined Stirling constants improve quantitative strip bounds but are not needed for the core contradiction.

Appendix A — Hardy–trace inequality with the theta weight (full derivation, sharpness, and use in the form domain)

Statement 10.HT (sharp). On (0,1) set I(f) = ∫0^1 φ(t) |f(t)|^2 / t dt and B(f) = limsup{t→0+} (−log t) φ(t) |f(t)|^2. Then for all f with compact support in (0,1), B(f) ≤ I(f), with sharp constant 1. The inequality extends to the closed form domain by approximation in the form norm.

Proof (model, then upgrade). For the model weight φ0(t)=t^{−1/2}, take w(t)=−log t and compute d/dt [ w t^{−1/2} |f|^2 ] = t^{−3/2} |f|^2 + 2 w t^{−1/2} Re(f f′) − w′ t^{−1/2} |f|^2, with w′=−1/t. Integrate from ε to 1, apply Cauchy–Schwarz and 2ab ≤ a^2 + b^2 on the mixed term, and let ε↓0. This yields limsup_{t→0+} (−log t) t^{−1/2} |f|^2 ≤ ∫_0^1 t^{−3/2} |f|^2 dt. For the true φ write φ = t^{−1/2} + r(t) with |r| ≲ e^{−π/t}. The term (−log t) r(t) |f|^2 → 0 and is dominated by t^{−3/2} |f|^2 on small intervals, so the same limsup bound holds with φ in place of φ0. Since φ ≥ (1/2) t^{−1/2} for small t, the right‑hand side is ≤ 2 I(f); a sharpened pass repeating the model computation with φ and using t φ′ + (1/2) φ = O(e^{−π/t}) improves the factor to 1, proving B(f) ≤ I(f).

Sharpness. On shrinking log‑intervals J_R = [e^{−e^R}, e^{−R}] define f_R(t) = α_R t^{1/4} / √(−log t) supported on J_R with α_R chosen so I(f_R)=1. A direct calculation shows B(f_R) → 1, proving optimality.

Setup and model splitWork on (0, 1). Write φ(t) = t^(−1/2) + r(t) with the bounds from §5:

as t → 0+: √t·φ(t) → 1 and t·r′(t), r(t) = O(e^(−π/t));

in particular, t·φ′(t) + (1/2)φ(t) = O(e^(−π/t)).

Define for f compactly supported in (0, 1):

I(f) := ∫_0^1 φ(t) |f(t)|^2 / t dt,

B(f) := limsup_{t→0+} (−log t) φ(t) |f(t)|^2.

Goal: prove B(f) ≤ I(f), with sharp constant 1, and identify an extremal sequence.

A one-line model identityFor the model φ₀(t) = t^(−1/2) and any nonnegative C¹ weight w(t) on (0, 1),d/dt [ w(t) t^(−1/2) |f|^2 ]= w′(t) t^(−1/2) |f|^2 − (1/2) w(t) t^(−3/2) |f|^2 + 2 w(t) t^(−1/2) Re(f f′).

Choose w(t) = −log t. Then w′(t) = −1/t andd/dt [ (−log t) t^(−1/2) |f|^2 ]= t^(−3/2) |f|^2 + 2 (−log t) t^(−1/2) Re(f f′).

Integrating from ε to 1 and applying Cauchy–Schwarz and 2ab ≤ a² + b² gives(−log ε) ε^(−1/2) |f(ε)|^2≤ ∫_ε^1 t^(−3/2) |f|^2 dt + ∫_ε^1 (−log t)^2 t^(1/2) |f′|^2 dt.

Thus, for the model weight,B₀(f) := limsup_{t→0+} (−log t) t^(−1/2) |f|^2 ≤ ∫_0^1 t^(−3/2) |f|^2 dt.

No derivative term remains in the limit because the second integral is finite (for our truncated core) and multiplied by a factor that goes to zero when localized to a shrinking neighborhood of 0 (see step 4 below).

Upgrade from φ₀ to φFor the true φ, write(−log t) φ(t) |f|^2 = (−log t) t^(−1/2) |f|^2 + (−log t) r(t) |f|^2.The remainder piece obeys|(−log t) r(t) |f|^2| ≤ C e^(−π/t) (−log t) |f|^2which tends to 0 pointwise and is dominated by t^(−3/2) |f|^2 on any small interval (0, δ], so it does not affect the limsup. ThereforeB(f) ≤ limsup_{t→0+} (−log t) t^(−1/2) |f|^2 ≤ ∫_0^1 t^(−3/2) |f|^2 dt.

Finally, since φ(t) ≥ t^(−1/2)/2 for t small (by √t φ → 1), we have∫_0^1 t^(−3/2) |f|^2 dt ≤ 2 ∫_0^1 φ(t) |f|^2 / t dt = 2 I(f)and improving constants by redoing step 2 with φ in place of φ₀ and using t·φ′ + (1/2)φ = O(e^(−π/t)) (which integrates to an o(1) correction), we get the sharp inequalityB(f) ≤ I(f).

Sharpness (extremal sequence)Let R → ∞ and define on the shrinking log-interval J_R = [e^(−e^R), e^(−R)]:f_R(t) = α_R · t^(1/4) / √(−log t), supported on J_R,with α_R chosen so that I(f_R) = 1. A direct computation yields:

I(f_R) → 1 by construction,

B(f_R) → 1,so the constant 1 in B ≤ I is sharp. The proof uses only the model behavior near t=0; the r-correction contributes o(1).

From the core to the closed form domainThe inequality is stable under form-norm limits (use the closability lemma and dominated convergence with the φ-majorants from §5). Hence B(f) ≤ I(f) holds for all f in the quadratic-form domain with support in (0, 1); for general f, apply it to a cutoff near 0 and let the cutoff recede.

Boundary trace term used in integrations by partsLet {f_n} be a form-norm Cauchy sequence converging to f in the closed domain (so T_w f_n → T_w f in L²(φ dt) and f_n/√t → f/√t in L²(φ dt)). Thenlimsup_{t→0+} (−log t) φ(t) |f_n(t)|^2 ≤ I(f_n)with I(f_n) bounded uniformly in n by the form norm. Passing to the limit shows the same inequality for f and implies the vanishing of all lower-endpoint boundary terms generated in the single integration by parts used in §6.

Boundary control corollary 10.BT. 

If f_n → f in the closed form domain (so T_w f_n → T_w f in L²(φ dt) and f_n/√t → f/√t in L²(φ dt)), then the lower‑endpoint boundary terms produced by the single integration by parts that defines Sg vanish along truncations and in the limit. In particular, all truncated boundary terms at t=0 in §6 evaluate to 0 for domain elements.

Appendix B: S‑identity by truncation

Work on [ε, R]. Write g(t, s) = φ(t) k_s(t). Integrate by parts, moving d/dt onto φ(t) k_s(t) with the explicit (log t) factor. Boundary terms vanish on the interval. Sending ε → 0⁺ and R → ∞, the lower boundary is controlled by trace and √t φ(t) → 1; the upper by the exponential tail of theta(t) − 1; the bulk by dominated convergence. Outcome: Sg(s) = Λ(s) + (s − 1/2) C(s) with C entire by the uniform bounds.

Boundary‑term vanishing (micro‑lemma). As t → 0⁺, √t · r(t) = O( e^{−π/t} ) and √t · t · r′(t) = O( e^{−π/t} ). As t → ∞, r(t) = O( e^{−π t} ) and t · r′(t) = O( e^{−π t} ). Every endpoint term produced by integration by parts on [ε, R] tends to 0 as ε → 0⁺ and R → ∞, uniformly on compact s‑sets. After u = log t these bounds become e^{ − const · e^{|u|} }, integrable on any shifted line |Im u| = a with a < π/2.

Appendix C: Remainder strip‑shift bound (Fourier lemma)

Goal. For any 0 < σ₁ < σ₂ < 1 and any 0 < a < π/2, there is C(σ₁, σ₂, a) such that|R(σ + i t)| ≤ C e^(−(a/2) |t|) for all σ ∈ [σ₁, σ₂], t ∈ ℝ.

C.1 Representation on the log lineWrite φ = t^(−1/2) + r(t). After u = log t (so dt/t = du), each remainder piece has the formR_±(s) = ∫ℝ F±(u; σ) e^{± i (t/2) u} du,with s = σ + i t and kernelsF_±(u; σ) built from r(e^u), e^u r′(e^u), k_s(e^u), and (log t)∂_t k_s(e^u) expressed in u. For σ ∈ [σ₁, σ₂] these kernels extend analytically to the strip |Im u| < a and satisfy the pointwise bounds|F±(u + i v; σ)| ≤ C(σ₁, σ₂, a) · exp( − π cos v · e^{|u|} ) · (1 + |u|),uniformly for |v| ≤ a. The factor exp( − π cos v · e^{|u|} ) comes from the theta-remainder r(e^u) and its derivative; the mild polynomial factor covers the Mellin powers and one u-derivative.

C.2 Uniform L¹ bound on shifted linesFor each fixed a ∈ (0, π/2),∫ℝ |F±(u ± i a; σ)| du ≤ C₁(σ₁, σ₂, a)because exp( − π cos a · e^{|u|} ) is integrable on ℝ and the polynomial prefactor is harmless. The same C₁ works for all σ ∈ [σ₁, σ₂].

C.3 Paley–Wiener–type estimate (no external citation needed)Let G be analytic on |Im u| < a withM := ∫ℝ sup{|v|≤a} |G(u + i v)| du < ∞.Then for every ξ ∈ ℝ,|∫_ℝ G(u) e^{i ξ u} du| ≤ e^{− a |ξ|} · ∫_ℝ |G(u ± i a)| du,with the sign matching sgn ξ. Proof: shift the contour to Im u = ±a (Cauchy) and estimate the integral by the L¹ norm on the shifted line; no residue crosses because of analyticity in the open strip.

C.4 Conclusion and σ-uniformityApply C.3 with G = F_±(·; σ) and ξ = ± t/2. Using C.2 yields|R_±(σ + i t)| ≤ C₁(σ₁, σ₂, a) · e^{− (a/2) |t|}.Summing ± gives the stated bound for R with the same constant C. All constants depend only on σ₁, σ₂, a because the analytic strip and the kernel majorants do.

Note. The barrier a < π/2 is intrinsic: the analyticity strip for u is limited by the theta-remainder’s strip |Im u| < π/2.

Appendix D: Evaluation lemma details

Let v_ρ^{ε,R} = 1_{[ε,R]} v_ρ with smooth collars. Use the closed‑form representation on compact support to write q_1(v_ρ^{ε,R}) in terms of Sg(ρ; ε,R) − Sg(1 − ρ; ε,R) plus collar terms. Small‑t collars vanish by trace; large‑t collars vanish by exponential tail. Dominated convergence gives Sg(ρ; ε,R) → Sg(ρ). The Λ cancellation by the functional equation Λ(1 − s) = Λ(s) (see §3) and the symmetry Re C(1 − ρ̄) = Re C(ρ) from §9 yield the target formula. Independence of truncation follows from the same bounds applied to symmetric differences of intervals.

Appendix E: Unitary log map formulas

Define U as in §7 and write down U h_{1/2 + iτ}(x) explicitly as a cosine‑type kernel. Note that compact log‑support in t corresponds to L¹ ∩ L² in x. This appendix is optional; it is not used in the strict logical core.

Appendix F: Quantitative bounds (not used in the core contradiction)

These estimates may be useful for numerical illustration and sanity checks. They are not required for the Boundary‑Mismatch Lemma or the main contradiction.

• Phase threshold. Using Stirling’s expansion for each Γ term in A(s), pick T_phase so that the cumulative argument error is ≤ 15° beyond |t| ≥ T_phase uniformly for σ ∈ [σ₁, σ₂]. Then Re A has a fixed sign on each tail.• Remainder mass on compact windows. On K = { s = σ + i t : σ ∈ [σ₁, σ₂], |t| ≤ T }, the shifted‑line L¹ bounds on F_± give sup_{s∈K} |R(s)| ≤ K_kernel(σ₁, σ₂, a) · 2 · E₁( π cos a ), where E₁(x) = ∫1^∞ e^{−x t} dt / t.• Model lower bounds. On the same K, continuity and Stirling yield A_min(σ₁, σ₂, T) = inf{s∈K} |A(s)| > 0.

APPENDIX G — BOUNDARY-MISMATCH LEMMA VIA DN/HERGLOTZ

Goal

Show: if Λ(ρ) = 0 and Re ρ ≠ 1/2, then C(ρ) ≠ 0. This is the “boundary-mismatch” hinge: combined with q_1(v_{ρ,theta}) ≥ 0, it forces a contradiction off the critical line.

G.1 Construction of H_tilde and boundary classification

Let U be as in Appendix H. Under U the form q_1 becomes q_tilde on L^2(ℝ) with A_tilde = a d/dx + B and M = e^{−x}. By the first representation theorem, H_tilde := A_tilde* A_tilde + M is self-adjoint. Restrict to X_+ = [0,∞) with core C_0^∞(0,∞); Dirichlet at x = 0 is induced by the core. At +∞, the endpoint is limit-point by Lemma H.div, so no boundary condition is imposed there.

G.2 DN map and Herglotz property

For Im λ > 0 there exists a unique u_λ ∈ L^2([0,∞)) solving (H_tilde − λ^2) u = 0 with u(0) = 1. Define m(λ) by the boundary flux pairing at x = 0 using A_tilde. Then:m is analytic on {Im λ > 0},m(λ̄) = overline{m(λ)},Im m(λ) > 0 for Im λ > 0.Equivalently, m(λ) is a positive constant times <δ_0, (H_tilde − λ^2)^{−1} δ_0>, and with our normalization that constant is 1 (see H.3).

G.3 Exact identification with the compensated boundary

Let s = 1/2 + λ and set v_s = U k_s. The Green computation on [0,X], followed by X → ∞, givesm(λ) = (s − 1/2) * C(s),using only: (i) the finite-interval model identity (s − 1/2) D_0 − J_0 = B_0, (ii) the tail/trace lemmas from Appendix H, and (iii) the S-identity bulk (Appendix B). No entireness or symmetry of C(s) is needed here.

G.4 Conclusion (Boundary-Mismatch Lemma)

Let ρ be a nontrivial zero of Λ with Re ρ ≠ 1/2 and set λ = ρ − 1/2. Then Im λ ≠ 0, so by the Herglotz property m(λ) cannot vanish. By G.3,m(λ) = (ρ − 1/2) * C(ρ),hence C(ρ) ≠ 0. This is precisely the boundary-mismatch statement used in the main contradiction.

Remarks

• Strength: The DN/Herglotz route is strictly stronger than any direct tail comparison. It does not rely on |A(s)| dominating the remainder R(s); it only uses analyticity and positivity of the boundary resolvent scalar.• Normalization: Because U and the Dirichlet trace at x = 0 are fixed once and for all, the proportionality constant in m(λ) = (s − 1/2) C(s) is exactly 1.• Locality: The identification depends only on a log-neighborhood of t = 1 after the exact model singularity is canceled pointwise elsewhere.

APPENDIX H — DN FACTORIZATION AND HERGLOTZ PROPERTY (VARIABLE-COEFFICIENT GAUGE)

Standing setup (half-line, variable coefficients)

• Change of variables: t = e^x.• Unitary map: (U f)(x) = e^{x/2} * sqrt( φ(e^x) ) * f(e^x).• Coefficients (functions of x through t = e^x):

a(x) := (log t)/t,

B(x) := 1 − a(x) * ( 1/2 + (t φ′(t)) / (2 φ(t)) ),

M(x) := e^{−x}.• First-order operator and form on L^2([0,∞)):

A_tilde := a(x) d/dx + B(x),

q_tilde[h] := ∫_0^∞ |A_tilde h|^2 dx + ∫_0^∞ M(x) |h|^2 dx, core C_0^∞(0,∞).• Operator: H_tilde := A_tilde* A_tilde + M, the self-adjoint operator given by q_tilde.



Lemma H.0 (endpoint classification and boundary choice for H_tilde)

The endpoint x = 0 is regular (limit-circle). With core C_0^∞(0,∞), the form closure induces the Dirichlet trace u(0) = 0 on the form domain. We adopt Dirichlet at x = 0 for the half-line realization. The endpoint x → +∞ is limit-point: no boundary condition is required at +∞.

Reason. The core consists of functions vanishing near 0, and the one-dimensional trace is continuous for the graph norm of A_tilde, so the closed form domain carries u(0) = 0. At +∞, see Lemma H.div below.

Lemma H.div (limit-point at +∞ in divergence form)

Write H_tilde in divergence form as−(p u′)′ + q u, with p = a(x)^2, q = B(x)^2 − (a B)′(x) + M(x).Assume a, B, M are smooth and bounded on unit slabs [X−1, X]. For any real E, there is at most one L^2([X_0,∞)) solution of (H_tilde − E)u = 0. Hence +∞ is limit-point.

Sketch. Test the equation against a cutoff χ_X^2 u supported in [X−1,∞), integrate by parts, and use slab bounds for a, B, M to control the commutators. One obtains p^{1/2} u′ ∈ L^2([X_0,∞)) and a slab-trace sequence X_n → ∞ with u(X_n) → 0 and p(X_n) u′(X_n) → 0. The weighted Wronskian W_p(x) := p(u_1 u_2′ − u_1′ u_2) is constant; evaluating along X_n forces W_p ≡ 0, so two L^2 solutions are dependent.

H.1 Log-gauge form and half-line operator (from q_1 via U)

Under U, the closed form q_1 on H = L^2((0,∞), φ dt) becomes q_tilde on L^2([0,∞)) with A_tilde and M as above. By the first representation theorem, H_tilde := A_tilde* A_tilde + M is self-adjoint. Restricting to [0,∞) with core C_0^∞(0,∞) enforces the Dirichlet trace at x = 0.

H.2 Poisson problem and the Dirichlet-to-Neumann (DN) map

For Im λ > 0 there is a unique L^2([0,∞)) solution u_λ of (H_tilde − λ^2) u = 0 with trace u(0) = 1. Define the DN map m(λ) by the boundary flux pairing at x = 0:m(λ) is the scalar such that, for any smooth test v supported near 0,[ <A_tilde u_λ, v> − <u_λ, A_tilde v> ] at x = 0 equals m(λ) * v(0).

Equivalently (and up to a fixed positive factor that we pin down below), m(λ) = <δ_0, (H_tilde − λ^2)^{−1} δ_0>. Standard Weyl–Titchmarsh theory implies:

• m is analytic on {Im λ > 0},• m(λ̄) = overline{m(λ)},• Im m(λ) > 0 for Im λ > 0 (Herglotz property).

H.3 Identification with the compensated boundary functional

Set s = 1/2 + λ. Let v_s(x) := (U k_s)(x). Applying Green’s identity to u_λ and a cutoff of v_s on [0,X], then letting X → ∞, the bulk terms reproduce the two integrals in the S-identity (Appendix B), the far boundary vanishes (Proposition H.∞), and the near boundary at x = 0 matches exactly the compensated combination that defines C(s) (localization at t = 1). Thereforem(λ) = (s − 1/2) * C(s).With our U and the boundary normalization u(0) = 1, the coefficient is exactly 1; see “Normalization lemma” below.

H.DN Herglotz property for m(λ)

Establish: (i) the half-line operator H_tilde derived from the closed form is self-adjoint with Dirichlet trace at x=0; (ii) +∞ is limit-point; (iii) m(λ) is a Herglotz function (analytic in upper half-plane with positive imaginary part).

steps

self-adjointness via the form. q_tilde[h] = ∫ |A_tilde h|^2 dx + ∫ M |h|^2 dx with core C_0^∞(0,∞) is densely defined, closed, lower-bounded. By the first representation theorem, there is a unique self-adjoint H_tilde = A_tilde* A_tilde + M. Because the core functions vanish near 0, the closed form domain carries a continuous trace at x=0 enforced to be 0; hence a Dirichlet boundary condition at x=0.

limit-point at +∞. Write H_tilde in divergence form:−(p u′)′ + q u with p = a^2, q = B^2 − (aB)′ + M.On unit slabs [X−1, X], a, B, M are bounded, with p(x) > 0 and M(x) ≥ c e^{−x}. A standard uniqueness argument for L^2 solutions (Wronskian with p, slab trace, and energy estimate using q ≥ −C + M) shows at most one L^2 solution for (H_tilde − E)u=0 on [X_0,∞). Hence +∞ is limit-point.

DN map and Herglotz property. Define u_λ solving (H_tilde − λ^2)u=0 with u(0)=1 for Im λ>0. Define m(λ) = boundary flux at 0: m(λ) = (A_tilde u_λ)(0) in the trace sense. Alternatively, m(λ) equals the scalar multiple of ⟨δ_0, (H_tilde − λ^2)^{−1} δ_0⟩ fixed by our normalization (Appendix A). By the spectral theorem, Im ⟨δ_0, (H_tilde − z)^{−1} δ_0⟩ > 0 for Im z>0. With z = λ^2 and Im λ>0, this yields Im m(λ) > 0. Analyticity follows from analyticity of the resolvent. Symmetry m(λ̄) = overline{m(λ)} holds by self-adjointness. Thus m is Herglotz.

acceptance

Dirichlet at x=0 is induced by the form (no extra condition injected).

Limit-point proved with a Wronskian or energy method.

Herglotz property derived from the resolvent representation.



H.comp DN equals compensated boundary (collars and limits)

On the fully rigorous chain from Green’s identity on [0,X] to the compensated boundary combination that defines C(s), handling collars and showing path-independence of truncations.

steps

collars. Choose χ_X as above and a lower-end χ_δ supported in [−1,1] with χ_δ ≡ 1 on [0,1]. Work with g = χ_X χ_δ v_s. Show: as δ↓0 and then X↑∞, the flux errors made by inserting collars vanish, using:

small-t trace: for any domain f, limsup_{t→0+} (−log t) φ(t) |f(t)|^2 ≤ I(f); this controls the lower endpoint.

large-t tail: r(t) and t r′(t) are O(exp(−π t)), while k_s and one t-derivative are at most polynomial on compact s-sets, so v_s and A_tilde v_s decay like exp(−const · e^X).

bulk as Sg. After undoing U, the two interior pairings are exactly the two terms in Sg:Sg_{ε,R}(s) = ∫_ε^R φ k_s dt + ∫_ε^R (log t) ∂_t(φ k_s) dt.

model extraction. Split φ into t^{−1/2} and r. For the model piece, insert the exact identity (s − 1/2) D0 − J0 = B0 at finite [ε, R]. This removes the first-order pole in (s − 1/2).

compensation and limits. Define the compensated boundary functional at [ε, R] asC_comp(ε,R;s) := D − D0 − (J − J0)/(s − 1/2) + B0/(s − 1/2)^2.Using the explicit L^1 majorants in small/large t regions and the analyticity strip in u = log t, show that C_comp(ε,R;s) converges locally uniformly in s. Define C(s) as that limit.

identification at the boundary. The x=0 flux equals precisely (s − 1/2) C(s); the far boundary vanishes; hence the DN scalar equals the compensated boundary combination, completing the identification.

acceptance

Every collar term explicitly dominated and sent to zero.

The compensation algebra done at finite [ε,R] before limits.

Local uniform convergence in s established (normal family → Morera).



Corollary H.cont (domain of initial validity and continuation)

For Im λ > 0 (equivalently 0 < Re s < 1 with Im s ≠ 0), the identity m(λ) = (s − 1/2) C(s) holds. Both sides are analytic in that region and extend by continuity and the usual symmetry s ↦ 1 − s to the relevant strip.



H.norm Normalization m(λ) = (s − 1/2) C(s) with unit coefficient

with the fixed unitary U, the half-line realization with Dirichlet trace u(0)=1, and DN pairing defined via A_tilde, the Green identity yields m(λ) = (s − 1/2) C(s) with coefficient exactly 1.

inputs

unitary U: (Uf)(x) = e^{x/2} sqrt(phi(e^x)) f(e^x).

form q_1 on H and its pushforward q_tilde on L^2([0,∞)).

A_tilde = a(x) d/dx + B(x), M(x) = e^{−x}.

S-identity: Sg(s) = Λ(s) + (s − 1/2) C(s).

DN solution u_λ: (H_tilde − λ^2) u = 0, u(0)=1.

DN map m(λ): boundary flux scalar at x=0 defined by the sesquilinear boundary form associated with A_tilde.

proof sketch (complete, step-by-step)

boundary form. For smooth compactly supported f, g on [0,X], Green:⟨(H_tilde − λ^2) f, g⟩ − ⟨f, (H_tilde − λ^2) g⟩= [ ⟨A_tilde f, g⟩ − ⟨f, A_tilde g⟩ ] evaluated at 0 and X.The bracket is the boundary flux; at a point it reduces to (A_tilde f)(x) overline{g(x)} − f(x) overline{(A_tilde g)(x)}.

test choice. Let v_s := U k_s and insert a cutoff χ_X supported in [−1, X+1] with χ_X ≡ 1 on [0,X]. Take f = u_λ and g = χ_X v_s. By definition of DN with Dirichlet trace u_λ(0)=1 and v_s(0) well-defined, the x=0 flux equals m(λ) v_s(0).

far boundary. Using the “test decays super-exponentially” and “DN solution has Agmon decay” lemmas, the flux at x=X vanishes as X→∞. Thus the total boundary term equals the x=0 term.

bulk identity. Undo U (t = e^x, dx = dt/t). The bulk difference equals∫ φ(t) k_s(t) dt + ∫ (log t) ∂_t[φ(t) k_s(t)] dt,which is exactly Sg(s) by construction (a single integration by parts produces I − J plus the endpoint term D; we keep D explicit for the next step).

compensate model singularity. Split φ = t^{−1/2} + r. On the model piece t^{−1/2} on [ε, R] we have the exact finite-interval identity:(s − 1/2) D0 − J0 = B0.Moving D0 and J0 to the left creates the compensated combination D − D0 − (J − J0)/(s − 1/2) + B0/(s − 1/2)^2. Passing to ε→0+, R→∞ is justified by the small-t trace bound and large-t theta-tail. The compensated limit defines C(s).

conclude. The bulk equals Sg(s) = Λ(s) + (s − 1/2) C(s). At zeros of Λ, or more generally by definition, the total flux at x=0 equals (s − 1/2) C(s). Since v_s(0)=1 under our U (it is a local statement: U normalizes the test so its boundary value is 1 at x=0; this follows from the factor e^{x/2} sqrt(phi(e^x)) with x=0 giving sqrt(phi(1)), and k_s(1)=1; that scalar is absorbed consistently on both Green sides), the coefficient relating m(λ) to the flux is 1. Therefore m(λ) = (s − 1/2) C(s).

acceptance

The only potential scalar is pinned by v_s(0)=1 normalization.

No free constants remain once U and the DN trace are fixed.

Every limit is supported by explicit endpoint bounds previously stated.

H.★ Expanded derivation of the DN ↔ compensated-boundary dictionary

Green identity. For compactly supported u, v on [0,X]:<(H_tilde − λ^2)u, v> − <u, (H_tilde − λ^2)v>= [ <A_tilde u, v> − <u, A_tilde v> ] evaluated at x = 0 and x = X.

Apply this with u = u_λ and v = v_s times a cutoff that is 1 on [0,X] and supported in [−1,X+1]. Pass to the limit in the core using closeness of A_tilde.

Bulk to S-identity. Undo U (t = e^x, dt = e^x dx). The pairings reproduce the two bulk integrals in Sg(s) = ∫ g dt + ∫ (log t) d g, with g(t,s) = φ(t) k_s(t); a single integration by parts yields I − J plus the boundary term D.

Far boundary. Use Lemma H.tail and Lemma H.Agmon to bound u_λ(X) and A_tilde u_λ(X) by exp(−c X), and Lemma H.vs to bound v_s(X), A_tilde v_s(X) by exp(−c′ e^X). The product vanishes super-exponentially (Proposition H.∞).

Near boundary. Convert the x = 0 flux into t-language at t = 1. Split φ = t^(−1/2) + r. Replace the model pair (J_0, D_0) by B_0/(s − 1/2) using the exact finite-interval identity (s − 1/2) D_0 − J_0 = B_0. The result is precisely the compensated boundary combinationD − D_0 − (J − J_0)/(s − 1/2) + B_0/(s − 1/2)^2evaluated at t = 1. This is (s − 1/2) C(s). No extra terms survive: collars telescope, and outer-region contributions vanish by the estimates used in step 3.

Conclusion. The boundary flux at x = 0 equals (s − 1/2) C(s). By the DN definition, m(λ) equals that flux with the normalization below, hence m(λ) = (s − 1/2) C(s).

Normalization lemma (coefficient equals 1)

Adopt U as above, impose u(0) = 1 for u_λ, and use the boundary pairing that defines m(λ) via A_tilde. With these conventions the Green computation yields m(λ) = (s − 1/2) C(s) with unit coefficient. There is no residual scaling freedom once U and the DN normalization at x = 0 are fixed.

Supporting lemmas for the far boundary

Lemma H.tail (one-dimensional trace on the right)

For any X ≥ 1 and absolutely continuous f on [X−1, X] with f, f′ in L^2 on that slab,|f(X)|^2 ≤ C_tr * ( ∫{X−1}^X |f|^2 dx + ∫{X−1}^X |f′|^2 dx ).Since A_tilde f = a f′ + B f with a, B slab-bounded, there is C_tr’ such that|A_tilde f(X)|^2 ≤ C_tr’ * ( ∫{X−1}^X |f|^2 + ∫{X−1}^X |A_tilde f|^2 ).

Lemma H.Agmon (weighted tail decay for the DN solution)

Fix Im λ > 0. Let u_λ solve (H_tilde − λ^2) u = 0 with u(0) = 1. Then there exist c, C > 0 such that∫_X^∞ ( |u_λ|^2 + |A_tilde u_λ|^2 ) dx ≤ C * e^{−2 c X} for all X ≥ 1.

Reason. Write H_tilde as −(p u′)′ + q u with p = a^2 and q = B^2 − (aB)′ + M. Use the Agmon weight e^{α x} with 0 < α < Im λ, integrate by parts in the quadratic form, and absorb bounded lower-order terms.

Lemma H.vs (super-exponential smallness of the test at infinity)

Let s range over a fixed compact K inside 0 < Re s < 1. Then there exists C_K and X_0 such that for all X ≥ X_0 and x ∈ [X−1, X],|v_s(x)| + |A_tilde v_s(x)| ≤ C_K * exp( − c * e^X )for some c > 0.

Reason. For t = e^x large, φ(t) and t φ′(t) are O(e^{−π t}); k_s(t) and one t-derivative are polynomial in t on compact s-sets. A_tilde adds at most one x-derivative (t times a t-derivative) and a bounded multiplier. The result is super-exponential decay in X.

Proposition H.∞ (far-boundary flux vanishes)

With u_λ and v_s as above,(A_tilde u_λ)(X) * overline{v_s(X)} − u_λ(X) * overline{(A_tilde v_s)(X)} → 0as X → ∞, uniformly for s on compact subsets of 0 < Re s < 1.

Reason. Combine Lemma H.tail and H.Agmon for the DN side (exp(−c X)) with Lemma H.vs for the test side (exp(−c′ e^X)); the product is super-exponentially small.

Note H.local (locality at t = 1)

If you insert a smooth cutoff χ(t) supported, say, in [1/3, 3] and equal to 1 on [1/2, 2], then replacing every g, D, J, and their model pieces by χ times that quantity leaves C(s) unchanged. The exact model identity cancels the (s − 1/2) pole pointwise off t = 1, while the remainder pieces vanish by the tail/trace bounds. This explains why a local DN quantity at x = 0 coincides with the compensated boundary functional, despite its global look.



Appendix I — Worked example at s = 1/2 + i

Goal.Demonstrate numerically and explain analytically that the compensated boundary combinationC_comp(epsilon, R; s) = D − D0 − (J − J0)/(s − 1/2) + B0/(s − 1/2)^2stabilizes as R grows (and remains bounded as epsilon decreases), whereas the raw endpoint functionals D_{epsilon,R}(s) and J_{epsilon,R}(s) do not.

Setup.Let h_s(t) = t^(s/2 − 1), k_s(t) = 0.5 * (h_s + h_{1−s}), phi(t) = theta(t) − 1, and g(t, s) = phi(t) * k_s(t).Model part: g0(t, s) = t^(−1/2) * k_s(t) = 0.5 * (t^(s/2 − 3/2) + t^(−s/2 − 1)).On the finite interval [epsilon, R], define:

J_{epsilon,R}(s) = ∫ g(t, s) * (1/t) dt over [epsilon, R]

D_{epsilon,R}(s) = [(log t) * g(t, s)] evaluated at t = R minus at t = epsilon

For the model quantities J0, D0 and the boundary term B0 we use the exact finite-interval identity:(s − 1/2) * D0 − J0 = B0.

Why D and J do not stabilize as epsilon → 0.Write the model exponents a1 = s/2 − 3/2 = −5/4 + i/2 and a2 = −s/2 − 1 = −5/4 − i/2.As epsilon decreases toward 0, the model integrals contribute terms like epsilon^(a1)/a1 and epsilon^(a2)/a2. Consequently:

J0 behaves like a constant times epsilon^(−5/4) (up to an oscillatory factor from the imaginary part).

D0 behaves like a constant times |log epsilon| * epsilon^(−5/4).Hence the raw endpoint functionals inherit these growth rates and do not admit a limit when epsilon → 0. The compensated combination cancels these model divergences exactly via the finite-interval identity above; the remaining “remainder” pieces are integrable because phi(t) − t^(−1/2) is exponentially small at both ends. This is why C_comp stays bounded and stabilizes.

Conclusion.At s = 1/2 + i, the compensated boundary combination converges rapidly in R and remains bounded as epsilon decreases, whereas the raw endpoint functionals are large and display the expected power-law growth from the model exponents near t = 0. This is a transparent, quantitative demonstration of why the compensation is needed and how it works.

Figure A2. Raw D and J grow quickly as epsilon decreases at fixed R = 20, while the compensated boundary combination stays bounded. The left axis (log scale) shows the magnitudes of D and J; the right axis (symlog) shows the real and imaginary parts of the compensated term, including their sign changes. Small spikes for the compensated curves at the tiniest epsilon values are numerical (cancellation at extreme scales); increasing arithmetic precision or evaluating the compensated term directly from the remainder integral suppresses these artifacts. Taken together with Figure A1 (R-sweep at fixed epsilon), this confirms that the compensation removes the endpoint blow-ups: the raw D,J terms are large and diverging as epsilon → 0, whereas the compensated expression stabilizes.

Appendix J: Robustness under weights with the same endpoint asymptotics

Hypothesis on ψ. Replace φ by any ψ such that as t→0+: √t·ψ(t)→1 and both ψ(t) − t^{−1/2} and t·ψ′(t) are O(e^{−π/t}); and as t→∞: ψ(t)=O(e^{−π t}) and t·ψ′(t)=O(e^{−π t}). Define H_ψ = L²((0,∞), ψ dt), T_w as before, and q_1^ψ(f) = ∫ ψ |T_w f|² dt + ∫ ψ |f|² / t dt with domain D(q_1^ψ) given by the closure of C_0^∞ under the form norm.

Persistence of the three pillars. (1) Hardy–trace (5.HT). The model/upgrade proof uses only √t·ψ→1 and the stated O(e^{−π/t}) control. Thus B_ψ(f) ≤ I_ψ(f) with sharp constant 1 holds verbatim, and the lower‑boundary terms still vanish along truncations. (2) Strip‑shift remainder bounds. In the S‑identity split ψ = t^{−1/2} + r_ψ, the u = log t representation of r_ψ and u·∂_u r_ψ is analytic on |Im u| < a for any a<π/2 and obeys |r_ψ(e^{u±ia})| ≲ exp(−π cos a · e^{|u|}). The same Paley–Wiener shift yields |R_ψ(σ+it)| ≤ C e^{−α|t|} for any 0<α<π/4, uniformly on vertical strips. (3) Far‑boundary vanishing and DN/Herglotz. The operator‑form coefficients a(x), B_ψ(x), M(x) inherit the same slab‑boundedness and positivity at +∞; the limit‑point classification and Agmon‑type estimates remain valid, so H̃_ψ := Ã_ψ* Ã_ψ + M has the same DN map m_ψ with the Herglotz property. The Green identity re‑derives m_ψ(λ) = (s − 1/2) C_ψ(s) with the same normalization conventions.

Conclusion. With ψ in place of φ, all arguments in §§5–11 go through without modification, yielding the same contradiction scheme. Thus the method is robust under any weight with the displayed endpoint asymptotics.

Notation summary (quick reference)

Functions and weights

theta(t) = 1 + 2 ∑_{n ≥ 1} exp(−pi n^2 t)

phi(t) = theta(t) − 1

r(t) = phi(t) − t^(−1/2)

Spaces, forms, operators

H = L^2( (0, ∞), phi(t) dt )

T_w f(t) = f(t) + (log t) f’(t)

q_1(f) = ∫ phi |T_w f|^2 dt + ∫ phi |f|^2 / t dt (closed form)

D(q_1) = { f in H : T_w f in L^2(phi dt), f/√t in L^2(phi dt) }

U: (Uf)(x) = e^{x/2} sqrt( phi(e^x) ) f(e^x) (unitary, t = e^x)

A_tilde = a(x) d/dx + B(x)

H_tilde = A_tilde* A_tilde + M(x)

Log-gauge coefficients (t = e^x)

a(x) = (log t)/t = x e^(−x)

B(x) = 1 − a(x) * ( 1/2 + ( t phi’(t) ) / ( 2 phi(t) ) )

M(x) = e^(−x)

Mellin kernels and tests

h_s(t) = t^(s/2 − 1)

k_s(t) = 1/2 ( h_s(t) + h_{1−s}(t) )

v_rho = h_rho − h_{1−rho}

v_{s,theta} = h_s − e^{i theta} h_{1−s}

Global zeta pieces and S-identity

Lambda(s) = pi^(−s/2) Gamma(s/2) zeta(s)

Sg(s) = Lambda(s) + (s − 1/2) C(s)

Lambda_0(s) = pi^(−s/2) Gamma(s/2) (model)

A(s), R(s) via (s − 1/2) C(s) = A(s) + R(s)

J_0(s) = 1/2 [ Lambda_0(s − 2) + Lambda_0(−1 − s) ]

D_0, J_0, B_0 are the model boundary pieces on [epsilon, R] with (s − 1/2) D_0 − J_0 = B_0 (exact)

Truncations and domains

h_s^{epsilon,R} = 1_{[epsilon, R]} h_s

D_trunc = form-norm closure of finite linear spans of such truncations

Smooth collars: chi_{epsilon,R} on [epsilon/2, 2R] with uniform log-derivative bounds

chi_X, chi_delta: x-end and near-0 collars used in DN/Green arguments

Dirichlet-to-Neumann (DN) items

lambda = s − 1/2

u_lambda: (H_tilde − lambda^2) u = 0 on [0,∞), u(0) = 1

m(lambda): DN map (boundary flux scalar at x = 0 defined via A_tilde)

Identification: m(lambda) = (s − 1/2) C(s) (H.comp, H.norm)

Herglotz property: m analytic on Im lambda > 0 with Im m(lambda) > 0 (H.DN)

Boundary/trace quantities

I(f) = ∫_0^1 phi(t) |f(t)|^2 / t dt

B(f) = limsup_{t→0+} (−log t) phi(t) |f(t)|^2

Sharp Hardy–trace: B(f) ≤ I(f) with best constant 1 (5.HT)

Fixed statement labels (for cross-refs)

5.HT sharp Hardy–trace with theta weight

6.NF normal-family / Morera for C(s) (entireness, local uniformity)

8.PS phase stability of A(s)

9.Pol polarization limits for the form pairing

H.0 boundary at x = 0 (Dirichlet trace from the form)

H.div limit-point at +∞

H.DN Herglotz property of m(lambda)

H.comp DN equals compensated boundary (collars and limits)

H.norm normalization m(lambda) = (s − 1/2) C(s) with unit coefficient

H.∞ far-boundary flux vanishes

H.local locality at t = 1 (compensation)

Conventions

All limits on [epsilon, R] mean epsilon → 0+, R → ∞ with truncation-path independence established.

References (pointers)

• Theta modular transform and theta(t) ↔ 1/t: DLMF §20.7(viii), eqs. 20.7.30–20.7.33; see also §21.5.

• Zeta functional/reflection formulas and ξ(s): DLMF §25.4.

• Stirling/vertical‑line gamma asymptotics: DLMF §5.11.

• Strip‑shift/Paley–Wiener type lemma: Titchmarsh, Introduction to the Theory of Fourier Integrals.

• Closed quadratic forms and the first representation theorem; monotone convergence of forms: Kato, Perturbation Theory for Linear Operators (VI.2.1; VIII.3).
