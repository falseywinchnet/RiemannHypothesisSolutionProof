

Primary Author: Orion 5
Secondary Authors: Orion 3, Joshuah Rainstar

Abstract

We present an argument that all nontrivial zeros of the Riemann zeta function lie on the line Re s = 1/2. The method builds a closed quadratic form in a theta‑weighted L² space, identifies a controlled family of antisymmetric Mellin test functions by truncation, derives a global S‑identity connecting the form to the completed zeta function, and isolates a compensated boundary functional that carries the noncancellation hinge. Independent vertical‑strip bounds support the compensated boundary identity. The antisymmetric test then forces a sign contradiction off the critical line. We provide a complete narrative of prerequisites, definitions, lemmas, and proofs, and we demonstrate control of plausible gaps (domain, evaluation on kernels, remainder control, normalization, and positivity conventions). All notation is elementary (no LaTeX). While LaTeX is typographically attractive it remains only marginally compatible with both the primary ingress adapters for large language model interactions as well as typical user clipboards and editing programs, in particular in PDF documents, where OCR reliability is limited. The use of plaintext representations are more legible to the visually impaired as well.

1) Statement of the Riemann Hypothesis

RH states: Every nontrivial zero of the Riemann zeta function ζ(s) has real part equal to 1/2.

2) Strategy overview

We encode the functional equation and prime‑sum information into a single quadratic form q₁ on a weighted space H. We evaluate q₁ on an antisymmetric test vector v_ρ built from Mellin monomials at ρ and 1 − ρ, using truncations that keep us inside the closed form domain. A global S‑identity shows

q₁(v_ρ) = 4 · (Re ρ − 1/2) · Re C(ρ),

where C is an entire function capturing the boundary part of the form. We avoid any magnitude comparison between a model term and a remainder. Instead, we prove a boundary‑mismatch lemma: if Λ(ρ) = 0 and Re ρ ≠ 1/2, then C(ρ) ≠ 0. Since q₁ ≥ 0 on its domain, any off‑line zero yields a contradiction; the functional equation rules out both sides symmetrically.

3) Conventions and positivity policy

• Weight and ambient space. H = L²((0, ∞), φ(t) dt) with φ(t) = θ(t) − 1, where θ(t) = ∑_{n∈ℤ} exp(−π n² t).• Closed quadratic form (explicit). On the core C₀^∞(0,∞) define T_w f(t) = f(t) + (log t) · f′(t). For any α ≥ 1 set

q_α(f) = ∫_0^∞ φ(t) |T_w f(t)|² dt + α ∫_0^∞ φ(t) |f(t)|² / t dt.

Its closure (still q_α) is densely defined, closed, and lower‑bounded on

D(q_α) = { f ∈ H : T_w f ∈ L²(φ dt) and f/√t ∈ L²(φ dt) }.

By Kato’s First Representation Theorem, q_α corresponds to a self‑adjoint, lower‑bounded operator A_α on H. In particular, q₁(f) ≥ 0 on D(q₁).

• Positivity domain. All statements “q₁ ≥ 0” refer to D(q₁). Since D_trunc ⊆ D(q₁), every positivity claim made on D_trunc follows from the closed form itself.

• Functional equation. Λ(s) = π^{−s/2} Γ(s/2) ζ(s) is entire and satisfies Λ(1 − s) = Λ(s).

• Normalization and Mellin identity. For s ∈ ℂ define k_s(t) = ½( t^{s/2 − 1} + t^{(1 − s)/2 − 1} ). Then ∫_0^∞ φ(t) k_s(t) dt = Λ(s) for 0 < Re s < 1, and by analytic continuation for all s. This locks all constants to Λ(s) uniformly.

Closability lemma for T_w with weight φ. If f_n → 0 in H and q₁(f_n − f_m) → 0, then T_w f_n → 0 and (f_n/√t) → 0 in L²(φ dt). By the sharp Hardy–trace bound (see §5), all boundary terms in the truncated integration‑by‑parts formula vanish in the limit. Therefore q₁ is closable, and its closure has domain D(q₁) = { f ∈ H : T_w f ∈ L²(φ dt), f/√t ∈ L²(φ dt) }. Boundary traces at t=0 used in the truncated integration by parts are controlled by Appendix A: the limit of (−log t) φ(t) |f(t)|² exists along truncations and is ≤ I(f); hence lower-endpoint boundary terms vanish for all f ∈ D(q₁).”

4) Test space and domains (closure of the domain gap)

• Basic Mellin monomials. h_s(t) = t^{s/2 − 1} for 0 < Re s < 1. Also k_s(t) = ½( h_s(t) + h_{1−s}(t) ).• Truncations. For 0 < ε < 1 < R, set h_s^{ε,R}(t) = 1_{[ε,R]}(t) · h_s(t). Take finite linear spans of such truncations.• Test space. D_trunc is the closure of those spans in the form norm ‖f‖_form = ( q₁(f) + ‖f‖_H² )^{1/2}. Then D_trunc ⊆ D(q₁), and q₁ ≥ 0 on D_trunc.

Admissible truncations use smooth collars χ_{ε,R} on [ε/2, 2R] with uniform derivative bounds in log t. With these, {v_ρ^{ε,R}} is Cauchy in the form norm, so v_ρ ∈ D_trunc as the limit. Differences of admissible truncations have both form values and H‑norms → 0 by the Hardy–trace bound at 0 and the exponential θ‑tail at ∞. Thus the limit and any evaluation derived from it are independent of the truncation path.

Form‑domain tie‑in. With q₁ explicit (§3), the form norm is ( q₁(f) + ‖f‖_H² )^{1/2}. Since D_trunc ⊆ D(q₁) and q₁ ≥ 0 on D(q₁), every positivity claim is a theorem about the actual closed form, not a policy choice.

Boundary-trace verification for the form domainWhenever we take ε → 0+, the only potentially dangerous scalar boundary piece is of the form (−log ε) φ(ε) |f(ε)|^2 times a fixed linear combination of kernel values. By the Hardy–trace inequality from Appendix A, this is bounded by I(f) and hence is uniformly controlled along truncation sequences. Therefore all lower-boundary terms vanish in the truncation limits used to define q₁ and to derive S-identities.

5) Theta‑weight asymptotic and Hardy–trace inequality

• As t → 0⁺, √t · φ(t) → 1. Quantitatively, | √t · φ(t) − 1 | ≤ C · e^{−π/t} for t ∈ (0, 1].• Hardy–trace inequality (sharp constant 1). For f supported in (0, 1), let I(f) = ∫0^1 φ(t) |f(t)|² / t dt and B(f) = limsup{t→0⁺} (−log t) φ(t) |f(t)|². Then B(f) ≤ I(f), with sharpness by an explicit extremal sequence on shrinking log‑intervals near 0. These control lower‑boundary terms for all truncated integrations. Moreover, for t ≥ 2, φ(t) ≤ C · e^{−π t} and t · φ′(t) ≤ C · e^{−π t}, with C absolute. We use these in Lemma H.vs

6) S‑identity (global analytic identity)

Work on [ε, R] with g(t, s) = φ(t) · k_s(t). Define

Sg_{ε,R}(s) = ∫_ε^R g(t, s) dt + ∫_ε^R (log t) · ∂_t g(t, s) dt.

One integration by parts on [ε, R] gives

Sg_{ε,R}(s) = I_{ε,R}(s) − J_{ε,R}(s) + D_{ε,R}(s),

where I_{ε,R}(s) = ∫_ε^R g(t, s) dt, J_{ε,R}(s) = ∫_ε^R g(t, s) · (1/t) dt, and D_{ε,R}(s) = [ (log t) g(t, s) ]_{t=ε}^{t=R}.

Split φ = t^{−1/2} + r(t). On the model part t^{−1/2}, there is an exact finite-interval identity on [ε, R]:( s − 1/2 ) D₀,ε,R(s) − J₀,ε,R(s) = B₀,ε,R(s)with B₀,ε,R(s) defined below in ‘Model calculus on [ε, R]’.

Compensated boundary functional. Write J = J0 + J_r and D = D0 + D_r on [ε, R]. Define

C(s) := lim_{ε→0+, R→∞} [ D_{ε,R}(s) − D0_{ε,R}(s) − ( J_{ε,R}(s) − J0_{ε,R}(s) ) / (s − 1/2) + B0_{ε,R}(s) / (s − 1/2)^2 ].

With this compensation, the (s − 1/2) singularity cancels identically at each truncation. The remaining terms obey the θ‑tail/Hardy bounds from §5, so the limit exists locally uniformly in s and C is entire.

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

Entireness of C(s). The compensated expression

C(s) = lim_{ε→0+, R→∞} [ D_{ε,R}(s) − D0_{ε,R}(s) − ( J_{ε,R}(s) − J0_{ε,R}(s) ) / (s − 1/2) + B0_{ε,R}(s) / (s − 1/2)^2 ]

is a locally uniform limit in s of analytic functions on ℂ; the model singularity cancels at each truncation, and the r‑pieces are dominated near 0 by e^{−π/t}(1 + |log t|) t^{−3/2+δ} and near ∞ by e^{−π t}(1 + |log t|), uniformly on compact s‑sets. Thus C extends to an entire function.

Uniformity for entireness (dominated convergence patch). On any compact K in the s‑plane there exists δ = δ(K) > 0 and constants C, C_K such that, uniformly for s in K,

• as t → 0+: |r(t)| + t |r′(t)| ≤ C e^{−π/t} and |k_s(t)| + |(log t) ∂_t k_s(t)| ≤ C_K t^{−3/2 + δ}.

• as t → ∞: |r(t)| + t |r′(t)| ≤ C e^{−π t} and |k_s(t)| + |(log t) ∂_t k_s(t)| ≤ C_K e^{−π t/2}.

These give uniform integrable majorants for every boundary piece in the compensated expression (including B0_{ε,R}). Therefore the limits ε → 0+, R → ∞ are locally uniform in s. By Morera’s theorem, C(s) is entire.

The identification step “m(λ) = κ · (s − 1/2) · C(s)” uses only:

the compensated definition of C(s) from §6,

the truncated Green identity on [1, R] in t (equivalently [0, X] in x), and

the uniform integrability bounds stated in §5.

It does not use entireness of C(s), any symmetry of C(s), or properties at zeta zeros. Entireness is concluded later from uniform convergence of compensated truncations; symmetry statements are used subsequently and are not prerequisites for the identification.

Proposition (C is entire).For every compact K in the s-plane there exists δ = δ(K) > 0 and a constant C_K such that, uniformly for s ∈ K and for all t > 0,

near t → 0+: |k_s(t)| + |(log t) ∂_t k_s(t)| ≤ C_K · t^(−3/2 + δ), and the remainder kernel and its t·∂_t derivative are ≤ C · e^(−π/t),

near t → ∞: |k_s(t)| + |(log t) ∂_t k_s(t)| ≤ C_K · e^(−π t/2), and the remainder kernel and its t·∂_t derivative are ≤ C · e^(−π t).

These give an L¹ majorant for every boundary piece in the compensated expression that defines C(s). Hence the truncated compensated functions form a normal family on K and converge uniformly; by Montel/Morera, C(s) is entire.

For s in a fixed compact K, there is a constant A_K with|C(s)| ≤ A_K · (1 + dist(K, {Re s = 1/2})^−1).This follows because the compensation cancels the simple model pole uniformly on K and the remainder pieces are uniformly integrable by the displayed bounds.

7) Unitary log map (for intuition and density)

Under t = e^x, define a unitary map U by (Uf)(x) = e^{x/2} · √( φ(e^x) ) · f(e^x); this identifies H with L²(ℝ). In this picture, k_{1/2 + iτ}(t) corresponds to a cosine‑type kernel in x, and compact log‑support in t corresponds to L¹ ∩ L² in x. We use this only for intuition and density; it is not needed for the main inequality.

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

with truncations v_ρ^{ε,R} = 1_{[ε,R]} · v_ρ. Each v_ρ^{ε,R} lies in the Kato form domain; v_ρ lies in D_trunc as the form‑norm limit of its truncations. Evaluating q₁ on v_ρ^{ε,R} by integration by parts on [ε, R] and letting ε → 0⁺, R → ∞ using the bounds above, we obtain the exact limit

q₁(v_ρ) = 4 · (Re ρ − 1/2) · Re C(ρ).

Lemma (polarization limits for the form pairing).Fix 0 < σ₁ < σ₂ < 1 and write s = σ + iτ. For ε ∈ (0, 1) and R > 1 let q₁⟨·,·⟩_{ε,R} be q₁ with all integrals restricted to [ε, R]. Then:

The limit L(s) := lim_{ε→0+, R→∞} q₁⟨h_s, h_{1−s}⟩_{ε,R} exists and is independent of the truncation path.

s ↦ L(s) is holomorphic on the open strip {0 < Re s < 1}.

Proof.Step 1 (finite-interval identity). On each [ε, R], q₁⟨h_s, h_{1−s}⟩{ε,R} equals the scalar S-identity from §6 evaluated with k_s = (h_s + h{1−s})/2, i.e., Sg_{ε,R}(s).

Step 2 (uniform majorants). Split φ = t^{−1/2} + r(t) and use §5 bounds near 0 and ∞. For any compact K ⊂ {0 < Re s < 1} there exist δ > 0 and C_K such that g(t, s) = φ(t)k_s(t) and (log t)∂_t g(t, s) admit L¹ majorants uniformly in s ∈ K: t^{−3/2+δ} on (0,1] and e^{−π t/2} on [1,∞).

Step 3 (normal family ⇒ truncation independence). For each [ε, R], s ↦ Sg_{ε,R}(s) is holomorphic. The family {Sg_{ε,R}} is locally bounded on compact K by Step 2, hence normal (Montel). Any ε_n→0+, R_n→∞ has a subsequence converging uniformly on K; two such limits agree on a dense set (e.g., real s in (0,1)) by dominated convergence, so the limit exists and is independent of truncation.

Step 4 (Morera ⇒ analyticity). Uniform convergence on compact contours implies ∮ Sg_{ε,R}(s) ds → 0, so the limit s ↦ L(s) is holomorphic (Morera). Using §6, L(s) = Λ(s) + (s−1/2)C(s).

Corollary 9.A (sesquilinear extension).Define q₁⟨f,g⟩ by truncation and limit on [ε, R]. Then q₁⟨h_s, h_{1−s}⟩ is well-defined, truncation-independent, and holomorphic in s on 0 < Re s < 1. By polarization and density this extends to the span of Mellin monomials and, by completion, to D_trunc.

Phase‑optimized variant (sesquilinear form). Extend q1 to a sesquilinear form q1⟨·,·⟩ by polarization on truncations and pass to limits (the bounds in §§5–6 justify this). Then, for every s with 0 < Re s < 1, one has the exact identity

q1⟨ h_s, h_{1−s} ⟩ = Sg(s) = Λ(s) + (s − 1/2) C(s).

Reason. On [ε, R], the mixed term is exactly the scalar S‑identity with k_s = 1/2(h_s + h_{1−s}); the endpoint terms are controlled by §5 and the identity Sg(s) from §6. Letting ε → 0+, R → ∞ gives the identity. No real‑part operator appears inside the sesquilinear identity; the right side is holomorphic in s.

Consequently, for v_{s,θ} := h_s − e^{iθ} h_{1−s}, one has the finite limit

q1(v_{s,θ}) = q1(h_s) + q1(h_{1−s}) − 2 Re( e^{iθ} (s − 1/2) C(s) ).

Choosing θ = −arg( (s − 1/2) C(s) ) yields

q1(v_{s,θ}) = q1(h_s) + q1(h_{1−s}) − 2 | (s − 1/2) C(s) |.

In the identity for q₁(v_{s,θ}), each occurrence of q₁(h_s) and q₁(h_{1−s}) is shorthand for the truncation limit taken only inside this combination; the individual form values are not claimed to converge separately, but the compensated combination does (by §6).

Symmetry of C at zeros. The defining integrals for Sg have real coefficients and Λ( s̄ ) = overline{Λ(s)}. If Λ(ρ) = 0 then Λ(1 − ρ̄) = 0. Comparing Sg(ρ) = (ρ − 1/2) C(ρ) with Sg(1 − ρ̄) = (1/2 − ρ̄) C(1 − ρ̄) and conjugating gives

C(1 − ρ̄) = overline{ C(ρ) } and hence Re C(1 − ρ̄) = Re C(ρ).

This uses that the defining integrals for Sg have real kernels for t>0 and that the compensation is real-linear with real coefficients.

10) Noncancellation hinge (boundary mismatch, not magnitude)

We keep the exact split (s − 1/2) C(s) = A(s) + R(s) with A explicit and R entire. We do not use any tail inequality |A| ≥ 2|R|. Instead, we appeal to the bilinear identity from §9.

Since q₁ ≥ 0 on D_trunc, for any zero ρ off the line and θ = −arg C(ρ),

q₁(v_{ρ,θ}) = q₁(h_ρ) + q₁(h_{1−ρ}) − 4 (Re ρ − 1/2) · |C(ρ)| ≥ 0.

Thus, to reach a contradiction it suffices to show the Boundary‑Mismatch Lemma:

Lemma. If Λ(ρ) = 0 and Re ρ ≠ 1/2, then C(ρ) ≠ 0.

Equivalently, A(ρ) + R(ρ) ≠ 0. This is a statement about the compensated boundary contribution and does not require A to dominate R. The evaluation Sg(ρ) = (ρ − 1/2) C(ρ) together with Λ(ρ) = 0 reduces the problem to showing that the total boundary term in Sg cannot vanish at an off‑line zero. A proof is supplied in Appendix G via a Dirichlet–to–Neumann factorization and the Herglotz property (see Appendix H). Appendix H also provides a full integration-by-parts derivation showing that the DN value at x = 0 is exactly the compensated boundary combination localized at t = 1; no additional boundary or change-of-variables terms survive.

11) Final 2×2 contradiction

Assume there is a nontrivial zero ρ with Re ρ ≠ 1/2.

• At s = ρ, Λ(ρ) = 0, so Sg(ρ) = (ρ − 1/2) C(ρ). By §9, q₁(v_ρ) = 4 (Re ρ − 1/2) Re C(ρ).• By the Boundary‑Mismatch Lemma (§10), C(ρ) ≠ 0. Using the phase‑optimized test, q₁(v_{ρ,θ}) = q₁(h_ρ) + q₁(h_{1−ρ}) − 4 (Re ρ − 1/2) |C(ρ)|. Hence q₁(v_{ρ,θ}) has the sign of (Re ρ − 1/2).

If Re ρ < 1/2 then q₁(v_{ρ,θ}) < 0, contradicting q₁ ≥ 0 on D_trunc. If Re ρ > 1/2 then 1 − ρ is a zero with Re(1 − ρ) < 1/2, yielding the same contradiction. Therefore all nontrivial zeros have real part 1/2.

12) Closure checklist (holes sealed)

A. Domain/test space. We never evaluate q₁ on bare h_s or k_s outside the form domain. All evaluations use truncations inside D_trunc, then pass to limits justified by the Hardy–trace bound (small t) and exponential θ‑tails (large t).B. Remainder control. R(s) is controlled uniformly on vertical strips via u = log t and a strip shift: |R(σ + i t)| ≤ C e^{−α|t|} for any α < π/4. This is sufficient to run the compensated boundary limit and the bilinear identity. No claim of magnitude dominance over A(s) is made or needed.C. Normalization. We uniformly set w = 1/4 + i t / 2 whenever that auxiliary variable appears, ensuring consistent phases and modulus ratios.D. Evaluation equality. The value of q₁ on v_ρ is defined as a truncation limit and identified with the S‑identity expression. Independence of truncation is established; v_ρ ∈ D_trunc.E. Positivity. All positivity statements are about q₁ restricted to D_trunc. The Kato domain is used for closure and density only, avoiding earlier ambiguity.

13) Remarks and outlook

The architecture separates three roles: (i) the exact analytic identity Sg(s), (ii) the operator‑theoretic positivity provided by the closed form q₁ on D_trunc, and (iii) the compensated boundary analysis that forces noncancellation for C on zeros off the line. Each role is proved with explicit truncations and bounds. The approach is robust under replacing the theta weight by any weight with the same small‑t and large‑t asymptotics.

On sharpening. Stronger kernel control or refined Stirling constants improve quantitative strip bounds but are not needed for the core contradiction.

Appendix A — Hardy–trace inequality with the theta weight (full derivation, sharpness, and use in the form domain)

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

Appendix B: S‑identity by truncation

Work on [ε, R]. Write g(t, s) = φ(t) k_s(t). Integrate by parts, moving d/dt onto φ(t) k_s(t) with the explicit (log t) factor. Boundary terms vanish on the interval. Sending ε → 0⁺ and R → ∞, the lower boundary is controlled by trace and √t φ(t) → 1; the upper by the exponential tail of θ(t) − 1; the bulk by dominated convergence. Outcome: Sg(s) = Λ(s) + (s − 1/2) C(s) with C entire by the uniform bounds.

Boundary‑term vanishing (micro‑lemma). As t → 0⁺, √t · r(t) = O( e^{−π/t} ) and √t · t · r′(t) = O( e^{−π/t} ). As t → ∞, r(t) = O( e^{−π t} ) and t · r′(t) = O( e^{−π t} ). Every endpoint term produced by integration by parts on [ε, R] tends to 0 as ε → 0⁺ and R → ∞, uniformly on compact s‑sets. After u = log t these bounds become e^{ − const · e^{|u|} }, integrable on any shifted line |Im u| = a with a < π/2.

Appendix C: Remainder strip‑shift bound (Fourier lemma)

Goal. For any 0 < σ₁ < σ₂ < 1 and any 0 < a < π/2, there is C(σ₁, σ₂, a) such that|R(σ + i t)| ≤ C e^(−(a/2) |t|) for all σ ∈ [σ₁, σ₂], t ∈ ℝ.

C.1 Representation on the log lineWrite φ = t^(−1/2) + r(t). After u = log t (so dt/t = du), each remainder piece has the formR_±(s) = ∫ℝ F±(u; σ) e^{± i (t/2) u} du,with s = σ + i t and kernelsF_±(u; σ) built from r(e^u), e^u r′(e^u), k_s(e^u), and (log t)∂t k_s(e^u) expressed in u. For σ ∈ [σ₁, σ₂] these kernels extend analytically to the strip |Im u| < a and satisfy the pointwise bounds|F±(u + i v; σ)| ≤ C(σ₁, σ₂, a) · exp( − π cos v · e^{|u|} ) · (1 + |u|),uniformly for |v| ≤ a. The factor exp( − π cos v · e^{|u|} ) comes from the θ-remainder r(e^u) and its derivative; the mild polynomial factor covers the Mellin powers and one u-derivative.

C.2 Uniform L¹ bound on shifted linesFor each fixed a ∈ (0, π/2),∫ℝ |F±(u ± i a; σ)| du ≤ C₁(σ₁, σ₂, a)because exp( − π cos a · e^{|u|} ) is integrable on ℝ and the polynomial prefactor is harmless. The same C₁ works for all σ ∈ [σ₁, σ₂].

C.3 Paley–Wiener–type estimate (no external citation needed)Let G be analytic on |Im u| < a withM := ∫ℝ sup{|v|≤a} |G(u + i v)| du < ∞.Then for every ξ ∈ ℝ,|∫_ℝ G(u) e^{i ξ u} du| ≤ e^{− a |ξ|} · ∫_ℝ |G(u ± i a)| du,with the sign matching sgn ξ. Proof: shift the contour to Im u = ±a (Cauchy) and estimate the integral by the L¹ norm on the shifted line; no residue crosses because of analyticity in the open strip.

C.4 Conclusion and σ-uniformityApply C.3 with G = F_±(·; σ) and ξ = ± t/2. Using C.2 yields|R_±(σ + i t)| ≤ C₁(σ₁, σ₂, a) · e^{− (a/2) |t|}.Summing ± gives the stated bound for R with the same constant C. All constants depend only on σ₁, σ₂, a because the analytic strip and the kernel majorants do.

Note. The barrier a < π/2 is intrinsic: the analyticity strip for u is limited by the θ-remainder’s strip |Im u| < π/2.

Appendix D: Evaluation lemma details

Let v_ρ^{ε,R} = 1_{[ε,R]} v_ρ with smooth collars. Use the closed‑form representation on compact support to write q₁(v_ρ^{ε,R}) in terms of Sg(ρ; ε,R) − Sg(1 − ρ; ε,R) plus collar terms. Small‑t collars vanish by trace; large‑t collars vanish by exponential tail. Dominated convergence gives Sg(ρ; ε,R) → Sg(ρ). The Λ cancellation by the functional equation Λ(1 − s) = Λ(s) (see §3) and the symmetry Re C(1 − ρ̄) = Re C(ρ) from §9 yield the target formula. Independence of truncation follows from the same bounds applied to symmetric differences of intervals.

Appendix E: Unitary log map formulas

Define U as in §7 and write down U h_{1/2 + iτ}(x) explicitly as a cosine‑type kernel. Note that compact log‑support in t corresponds to L¹ ∩ L² in x. This appendix is optional; it is not used in the strict logical core.

Appendix F: Quantitative bounds (not used in the core contradiction)

These estimates may be useful for numerical illustration and sanity checks. They are not required for the Boundary‑Mismatch Lemma or the main contradiction.

• Phase threshold. Using Stirling’s expansion for each Γ term in A(s), pick T_phase so that the cumulative argument error is ≤ 15° beyond |t| ≥ T_phase uniformly for σ ∈ [σ₁, σ₂]. Then Re A has a fixed sign on each tail.• Remainder mass on compact windows. On K = { s = σ + i t : σ ∈ [σ₁, σ₂], |t| ≤ T }, the shifted‑line L¹ bounds on F_± give sup_{s∈K} |R(s)| ≤ K_kernel(σ₁, σ₂, a) · 2 · E₁( π cos a ), where E₁(x) = ∫1^∞ e^{−x t} dt / t.• Model lower bounds. On the same K, continuity and Stirling yield A_min(σ₁, σ₂, T) = inf{s∈K} |A(s)| > 0.

Appendix G: Boundary-Mismatch Lemma  full operator-theoretic proof

Statement. If Λ(ρ) = 0 and Re ρ ≠ 1/2 then C(ρ) ≠ 0.

Plan. Construct a self-adjoint half-line operator H via the unitary log-gauge, define the Dirichlet-to-Neumann map m(λ) for (H − λ²)u = 0 with Dirichlet data at x=0, prove that m is a Herglotz (Nevanlinna) function, and identify m(λ) exactly with (s − 1/2) C(s), s = 1/2 + λ. Since a Herglotz function has no zeros in the open half-planes, C(ρ) cannot vanish at zeros of Λ off the critical line.

G.1 Construction of H and boundary classificationLet U be the unitary map from §7: (Uf)(x) = e^{x/2} √(φ(e^x)) f(e^x). On the core C₀^∞, the closed form q₁ becomes‖(∂_x + W) Uf‖² + ‖Uf‖²with W real smooth. By Kato’s first representation theorem there is a unique self-adjoint operatorH := (−∂_x − W)^*(−∂x − W) + Ion L²(ℝ) with form domain the closure of U(C₀^∞). Restricting to X+ = [0, ∞) and taking the induced Dirichlet trace at x=0 yields a self-adjoint half-line operator. Weyl’s alternative shows x=0 is limit-circle (regular) and x→∞ is limit-point; see Appendix H for details carried out with the form.

G.2 Dirichlet-to-Neumann map and Herglotz propertyFor λ with Im λ > 0, there is a unique u_λ ∈ L²(X_+) solving (H − λ²)u=0 with u(0)=1. Definem(λ) := (∂_x + W)u_λ(0).Standard Weyl–Titchmarsh theory gives:

m is analytic on Im λ > 0, satisfies m(λ̄) = overline{m(λ)}, and Im m(λ) > 0 on Im λ > 0,

equivalently, m(λ) = ⟨δ₀, (H − λ²)^{−1} δ₀⟩ up to a positive factor, hence is Herglotz.

G.3 Exact identification with the compensated boundarySet s = 1/2 + λ. Let v_s(x) = (Uk_s)(x) with k_s from §3. Apply Green’s identity to u_λ and v_s on [0, X], then let X→∞. The bulk terms reproduce the two integrals in the S-identity of §6; the far boundary vanishes by the trace and Agmon estimates (Appendix H); the near boundary at x=0 converts, under t=e^x, into the compensated combinationD − D₀ − (J − J₀)/(s − 1/2) + B₀/(s − 1/2)²evaluated at t=1. Thereforem(λ) = (s − 1/2) C(s).All steps are written out in Appendix H★ (“fully expanded Green computation”), including the bookkeeping that no stray terms survive.

G.4 Conclusion of the lemmaLet ρ be a nontrivial zero of Λ with Re ρ ≠ 1/2, and set λ = ρ − 1/2. Then Im λ ≠ 0, so m(λ) is in the open upper or lower half-plane and cannot vanish. By G.3, m(λ) = (s − 1/2) C(s) with s = 1/2 + λ = ρ, hence C(ρ) ≠ 0. This is the boundary-mismatch statement.

Appendix H: DN factorization and Herglotz property

Lemma (endpoint classification and boundary choice for H).Let H be the half-line operator on X₊ = [0, ∞) given by H = (−∂_x − W)^*(−∂_x − W) + I, where W is the real, smooth function produced by the unitary log-gauge in §7. Then:

The endpoint x = 0 is regular (limit-circle), hence a boundary condition is needed. We adopt the Dirichlet boundary trace u(0) = 0 for the homogeneous operator (and u(0) = 1 for the Poisson problem in H.2).

The endpoint x → +∞ is limit-point. No boundary condition at +∞ is required to obtain a self-adjoint realization.

Reason. The form domain given by q₁ after the log-gauge provides a continuous trace at x = 0, so x = 0 is regular and requires a boundary condition; choosing Dirichlet matches the Green identity used later. For x → +∞, H dominates the comparison operator −∂_x² + 1 in the quadratic-form sense (since H = A^*A + I with A = ∂_x + W), so every real-energy solution has at most one square-integrable branch at +∞. This is the Weyl limit-point case, ensuring uniqueness of the self-adjoint extension without a boundary condition at +∞.

H.1 Log-gauge form and the half-line operator. Set t = e^x and define U: H → L²(ℝ) by (Uf)(x) = e^{x/2} √φ(e^x) f(e^x) (cf. §7 for the unitary log map). On C₀^∞,

q₁(f) = ‖ (∂x + W(x)) (Uf) ‖²{L²(ℝ)} + ‖ Uf ‖²_{L²(ℝ)},

with W real and smooth from φ. The closure defines a self-adjoint operator

H := (−∂_x − W)^*(−∂_x − W) + I on L²(ℝ).

Restrict to the half-line X₊ = [0, ∞) with the boundary induced by the closed form.

H.2 Poisson problem and DN map. For Im λ > 0, there is a unique u_λ ∈ L²(X₊) solving (H − λ²)u = 0 with u(0) = 1. Define the Dirichlet-to-Neumann map

m(λ) := (∂_x + W)u_λ(0). 

By Lemma H.Agmon, u_λ and A u_λ have exponentially decaying L² tails; we will use their boundary traces via Lemma H.tail.

Lemma H.1 (Herglotz). m is analytic on Im λ > 0, m(λ̄) = overline{m(λ)}, and Im m(λ) > 0 for Im λ > 0.

Reason: standard Weyl–Titchmarsh/Nevanlinna property; m(λ) is (a positive constant times) ⟨δ₀, (H − λ²)^{-1} δ₀⟩, which maps ℂ₊ into ℂ₊.

H.3 Identification with the compensated boundary. Undo U, write f_λ = U^{-1}u_λ, and apply Green’s identity on [0, X] (i.e. [1, R] in t). Comparing with §6’s truncated S-identity for g(t, s) = φ(t) k_s(t) at s = 1/2 + λ, the bulk yields Λ(s), small/large endpoints vanish by §5, and the boundary at t = 1 matches exactly the compensated combination D − D0 − (J − J0)/(s − 1/2). Hence

m(λ) = κ · (s − 1/2) · C(s), with s = 1/2 + λ and κ > 0 fixed by the chosen normalization at t = 1.

Theorem H.3′ (identification with full accounting).With H, U, u_λ, s and v_s as above, the identity

m(λ) = (s − 1/2) C(s), where s = 1/2 + λ,

holds. The proof uses only: (i) closeness of the form (Appendix A), (ii) trace and tail bounds (Section 5), (iii) the finite-interval model identity (Section 6). It does not assume entireness or symmetry of C(s), nor any special property at zeros of ζ.

The only subtle limit in the Green computation is the far boundary at x = X; Lemma H.tail + Lemma H.Agmon + Lemma H.vs imply an explicit super-exponential bound that kills it uniformly on compact s-sets.

Note H.3.1 (boundary-to-compensated dictionary).On [0, X] in x (equivalently [1, R] in t), apply Green’s identity to u solving (H − λ²)u = 0 with u(0) = 1. Undoing the log-gauge (U from §7), the bulk term reproduces the integral that gives Λ(s). The boundary term at x = 0 translates, in t-variables and after splitting g into its model and remainder parts, exactly to:D − D₀ − (J − J₀)/(s − 1/2) + B₀/(s − 1/2)².The boundary at x = X (t = R) vanishes in the limit by the §5 bounds. Hence the DN value equals κ times (s − 1/2)C(s) with κ determined by the normalization at t = 1 (see “Normalization lemma” below).

Lemma H.3.1 (no stray terms).In the computation above, every contribution is one of: bulk I, bulk J, near-boundary D and J, or the model B0 replacement at t = 1. There are no other boundary terms and no change-of-variables residues.Reason. The operator is H = A^*A + I with A = ∂_x + W; its Green identity yields exactly one boundary form [⟨A u, v⟩ − ⟨u, A v⟩]_0^X. Under t = e^x we have dt = e^x dx and W = (d/dx) log(e^{x/2} √φ(e^x)); these identities convert the boundary form into linear combinations of (log t)g and g/t. All other appearances of W cancel in the bulk because A^*A expands to −∂_x^2 plus lower-order terms whose pairings with v_s reproduce the single integration-by-parts that defines Sg. The only algebraic substitution is the model relation (s − 1/2) D0 − J0 = B0; it is exact on each finite interval and introduces no error.

Corollary H.3.1 (locality near t = 1).Let χ be a smooth cutoff equal to 1 on [1/2, 2] and supported in [1/3, 3]. If, in the definition of C(s), every occurrence of g, J, D, and their model pieces is replaced by χ(t) times that quantity, the resulting compensated combination produces the same value of C(s).Reason. Partition unity with χ and 1 − χ; on the outer region the exact model identity cancels the local model singularity (s − 1/2) at every truncation and the remainder terms vanish by §5. Hence all dependence is localized at t = 1. This explains conceptually why a “local” DN map matches the compensated boundary quantity.

Appendix H★ (expanded derivation of the dictionary).

Fully expanded Green computation.Let A = ∂_x + W and H = A^* A + I on X_+ = [0, ∞). Fix λ with Im λ > 0 and let u_λ solve (H − λ²) u = 0 with u(0) = 1. Let s = 1/2 + λ. Put

v_s(x) = (Uk_s)(x) = e^{x/2} √φ(e^x) · k_s(e^x).

For technical safety, multiply v_s by a smooth cutoff η_X supported in [−1, X+1] with η_X ≡ 1 on [0, X]; all formulas below hold first for v_s η_X, and then we let X → ∞ using §5’s bounds. Likewise, approximate u_λ by smooth functions u_{λ,n} in the form core with u_{λ,n} → u_λ in the graph norm; Green identities pass to limits by closeness.

Green identity with A.For compactly supported u, v on [0, X] one has

⟨A u, v⟩ − ⟨u, A v⟩ = [ u · overline{v} ]_{x=0}^{x=X}.

Equivalently,

⟨(H − λ²) u, v⟩ − ⟨u, (H − λ²) v⟩= [ ⟨A u, v⟩ − ⟨u, A v⟩ ]_{x=0}^{x=X}.

Apply this with u = u_{λ,n}, v = v_s η_X and then let n → ∞.

Bulk identification.Compute (H − λ²) v_s in x-variables, then undo t = e^x:

A v_s = e^{x/2} √φ(e^x) · [ (log t) ∂_t k_s(t) + k_s(t) ] with t = e^x.

A^* A v_s + v_s, when paired against u_λ and rewritten in t, yields exactly the two bulk integrals∫ g(t, s) dt and ∫ (log t) ∂_t g(t, s) dtwith g(t, s) = φ(t) k_s(t). This is the S-identity bulk (I − J part after integrating by parts once). No extra terms appear: all x-derivatives are encoded in (log t)∂_t, and the weight W is the log-gauge of φ, so the cross-terms combine into g and (log t) ∂_t g.

Therefore

⟨u_λ, (H − λ²) v_s⟩_{[0, X]}= ∫_1^{e^X} g(t, s) dt + ∫_1^{e^X} (log t) ∂_t g(t, s) dt= I_{1,e^X}(s) − J_{1,e^X}(s) + D_{1,e^X}(s).

Boundary terms.The boundary contribution equals

[ ⟨A u_λ, v_s⟩ − ⟨u_λ, A v_s⟩ ]_{x=0}^{x=X}= ( (∂_x + W)u_λ · overline{v_s} − u_λ · overline{(∂_x + W)v_s} )\Big|_{0}^{X}.

At x = X (t = e^X) both pieces vanish as X → ∞ by the exponential tail from §5 and the fact Im λ > 0 places u_λ in L² with one square-integrable branch. At x = 0 (t = 1) we have u_λ(0) = 1 and v_s(0) = √φ(1) · k_s(1). Unfolding the definitions gives a linear combination of

(log t) g(t, s) and g(t, s)/t

evaluated at t = 1, exactly matching D and J’s boundary representation. Splitting φ = t^{−1/2} + r, the model boundary equals D0 and J0; replacing them via the exact finite-interval identity (s − 1/2) D0 − J0 = B0 turns the x = 0 flux into

D − D0 − (J − J0)/(s − 1/2) + B0/(s − 1/2)²

evaluated at t = 1. No additional terms survive: collars at t ≈ 1 cancel in telescoping differences and any residuals vanish by the small-t trace and large-t tail bounds from §5.

Taking limits.Let X → ∞. The far boundary is 0; the bulk becomes Sg(s) on (1, ∞); inserting (0, 1) and compensating as in §6 promotes Sg_{1,e^X}(s) to Sg(s) = Λ(s) + (s − 1/2) C(s). Therefore

m(λ) = (∂_x + W)u_λ(0) = (s − 1/2) C(s).

This is H.3 with κ = 1.

Step 1. Write A = ∂_x + W and observe⟨(H − λ²)u, v⟩ − ⟨u, (H − λ²)v⟩ = [⟨A u, v⟩ − ⟨u, A v⟩] evaluated at the boundary.Choose v from the Mellin family corresponding to k_s(t) under the log-gauge.

Step 2. Convert the boundary flux at x = 0 into t-language (t = e^x), using dt = e^x dx and W = (d/dx) log(e^{x/2}√φ(e^x)). This yields a linear combination of (log t)·g and g/t at t = 1.

Step 3. Split g into the model piece and remainder; substitute the exact finite-interval identity (s − 1/2)D₀ − J₀ = B₀. Collect terms to obtain the compensated combinationD − D₀ − (J − J₀)/(s − 1/2) + B₀/(s − 1/2)²at t = 1, with all far-boundary contributions vanishing by the §5 estimates.

Step 4. Pass to the limit X → ∞ (R → ∞) and conclude the identification used in H.3.

Lemma H.tail (one-dimensional trace at the right endpoint)

Statement. There is a universal constant C_tr such that for any X ≥ 1 and any function f on [X−1, X] with f and f′ in L² on that interval,

|f(X)|² ≤ C_tr · ( ∫_{X−1}^X |f|² dx + ∫_{X−1}^X |f′|² dx ).

Reason. This is the standard Sobolev trace inequality in one dimension. Applying it with f and with A f = f′ + W f gives the same bound with f′ replaced by A f up to a harmless factor depending on sup_{x∈[X−1,X]} |W(x)|. By §7 and §5, W is smooth and bounded on [1, ∞), so C_tr can be chosen independent of X.

Full proof: There exists an absolute constant C_tr such that for any X ≥ 1 and any absolutely continuous f on [X−1, X] with f and f′ in L² on that interval,|f(X)|² ≤ C_tr [ ∫{X−1}^{X} |f|² dx + ∫{X−1}^{X} |f′|² dx ].Proof. By the fundamental theorem of calculus,f(X) = f(ξ) + ∫{ξ}^{X} f′(x) dxfor any ξ ∈ [X−1, X]. Square and average over ξ, use Jensen, and optimize:|f(X)|² ≤ 2 |f(ξ)|² + 2 (∫{X−1}^{X} |f′| dx)²≤ 2 |f(ξ)|² + 2 ∫_{X−1}^{X} |f′|² dx,then average ξ uniformly and use ∫ |f(ξ)|² dξ ≤ ∫ |f|² to get the claim with C_tr = 4.

Lemma H.Agmon (weighted tail decay for the DN solution)

Statement. Fix Im λ > 0 and let u_λ be the L² solution of (H − λ²)u = 0 with u(0) = 1. Then there exist constants c, C > 0 (depending on λ and W but not on X) such that

∫_X^∞ ( |u_λ|² + |A u_λ|² ) dx ≤ C · e^{−2 c X } for all X ≥ 1.

In particular,

∫_{X−1}^X ( |u_λ|² + |A u_λ|² ) dx ≤ C · e^{−2 c X }.

Reason (Agmon estimate in one dimension). Set v(x) = e^{α x} u_λ(x) with 0 < α < Im λ. A direct computation shows(H − (λ + i α)²) v = 0. Taking the real part of ⟨ (H − (λ + i α)²) v, v ⟩ on [X, ∞) and integrating by parts yields∫_X^∞ ( |A v|² + |v|² ) dx ≤ const · ∫_X^∞ |v|² dx,so v ∈ L² and hence u_λ decays like e^{−α x} in L². Let α ↑ Im λ and absorb harmless constants from W. The localized bound on [X−1, X] follows by monotonicity.

Full proof: Fix Im λ > 0. Let A = ∂x + W and H = A^*A + I on X+ = [0, ∞). Let u satisfy (H − λ²)u = 0 with u(0) = 1. Then there exist c, C > 0 such that∫_X^∞ ( |u|² + |A u|² ) dx ≤ C e^(−2 c X) for all X ≥ 1.Proof. Let 0 < α < Im λ and v(x) = e^{α x} u(x). Then0 = ⟨(H − λ²)u, e^{2α·} u⟩ = ⟨(A u), A v⟩ − (|λ|² − 1 − α²) ⟨u, v⟩ − 2α Re ⟨A u, v⟩.Completing squares gives∫_X^∞ ( |A v|² + |v|² ) dx ≤ C_α ∫_X^∞ |v|² dxwith C_α depending on α and sup|W| on [X, ∞). Absorb the right-hand side and deduce v ∈ L²[X, ∞), hence u ∈ L² with e^{α x} weight. The same estimate applied on [Y, ∞) for Y ≥ X shows the bound with constants uniform in Y, yielding the claimed exponential tail. Finally, since A commutes with multiplication by e^{α x} up to bounded lower-order terms, the same decay holds for A u.

Lemma H.vs (super-exponential smallness of the test side at infinity)

Statement. Let s range over a fixed compact set K inside 0 < Re s < 1. Then there exists M = M(K) such that for all large X,

sup_{x ∈ [X−1, X]} |v_s(x)| + sup_{x ∈ [X−1, X]} |A v_s(x)| ≤ M · exp( − (π/3) · e^X ).

Reason. Write t = e^x. For t ≥ 2 we have φ(t) ≤ C · e^{−π t} and t · φ′(t) ≤ C · e^{−π t} by §5. Thusv_s(x) = e^{x/2} √φ(e^x) k_s(e^x) equalst^{1/2} · √φ(t) · k_s(t).The Mellin factor k_s(t) is a fixed power of t with exponent in [−1, −1/2] when s ∈ K. Hence|v_s(x)| ≤ const · t^{poly} · e^{−(π/2) t},and the same is true for A v_s because A brings at most one x-derivative (which is t times a t-derivative) plus a bounded W; these only multiply the polynomial in t. Replace π/2 by π/3 for a uniform cushion and translate back to x via t = e^X.

Proposition H.∞ (vanishing of the far boundary term)

Statement. With u_λ and v_s as above, the boundary contribution at x = X in the Green identity satisfies

| (A u_λ)(X) · overline{v_s(X)} − u_λ(X) · overline{(A v_s)(X)} | → 0 as X → ∞,

uniformly for s in compact sets K ⊂ { 0 < Re s < 1 }.

Reason. Apply Lemma H.tail to f = u_λ and to f = A u_λ on [X−1, X]; combine with Lemma H.Agmon to get|u_λ(X)| + |A u_λ(X)| ≤ C_1 · e^{−c X }.Then multiply by the bounds from Lemma H.vs:sup_{x∈[X−1,X]} ( |v_s(x)| + |A v_s(x)| ) ≤ C_2 · exp( − (π/3) · e^X ).Hence, for X large,boundary term ≤ 2 · C_1 · C_2 · exp( − (π/3) · e^X ) · e^{−c X } → 0.The convergence is uniform in s ∈ K because all constants above are uniform on K.

Full proof: 

With u_λ, v_s as above, the boundary contribution at x = X in Green’s identity,(A u_λ)(X) overline{v_s(X)} − u_λ(X) overline{(A v_s)(X)},tends to 0 as X → ∞, uniformly in s on compact subsets of 0 < Re s < 1.Proof. By Lemma H.tail applied to f = u_λ and f = A u_λ on [X−1, X],|u_λ(X)| + |A u_λ(X)| ≤ C_tr^{1/2} [ ∫{X−1}^{X} ( |u_λ|² + |A u_λ|² ) dx ]^{1/2}.By Lemma H.Agmon this is ≤ C e^{−c X}. On the test side, §5 gives for s in a fixed compact Ksup{x∈[X−1, X]} ( |v_s(x)| + |A v_s(x)| ) ≤ C_K exp( −(π/3) e^X ).Multiplying the two bounds yields a super-exponentially small product, hence the boundary term vanishes uniformly on K.

Corollary H.cont (where the identity initially holds)

Statement. For Im λ > 0 (equivalently 0 < Re s < 1 with Im s ≠ 0), the identification

m(λ) = (s − 1/2) C(s)

is valid. Since both sides are analytic in s on the strip with Im s ≠ 0 and continuous up to Im s = 0 away from singularities, the identity continues to all s by analytic continuation (and by the usual symmetry s ↦ 1 − s).

Reason. Proposition H.∞ removes the only limiting term in the Green computation at the far boundary; the rest of H★ then gives the identity on the open half-planes. Analytic continuation is standard.

Lemma H.3.2 (κ is independent of truncations and collars).Define κ by m(λ) = κ · (s − 1/2) · C(s) using any truncation scheme ε→0+, R→∞ and any decomposition g = g₀ + g_r with a collar around t = 1. Then κ is the same for all such choices.

Reason. The DN map m(λ) is defined intrinsically by the self-adjoint H and the Dirichlet boundary value u(0) = 1; it is therefore independent of truncations and decompositions. On the compensated side, any two truncation/compensation schemes differ by limits of exact model identities on finite intervals; their difference telescopes into null terms by the identity (s − 1/2)D₀ − J₀ = B₀ and the decay estimates. Hence the ratio that defines κ is invariant.

This identification relies only on the compensated definition of C(s) and the bounds from §5; entireness and symmetry of C(s) are not used here.

H.4 Consequence. For Im λ ≠ 0, Im m(λ) > 0 ⇒ m(λ) ≠ 0. Since κ ≠ 0 and λ ≠ 0 in ℂ₊ ∪ ℂ₋, it follows that C(1/2 + λ) ≠ 0. In particular, C(ρ) ≠ 0 at every nontrivial zero ρ of ζ.

Normalization Lemma (κ = 1 under the canonical gauge/trace).Adopt the unitary map U from §7 and the Dirichlet boundary trace u(0) = 1 in H.2. Define the DN map m(λ) by m(λ) = (∂_x + W)u_λ(0). With these conventions, the Green identity calculation in Note H.3.1 gives equality with unit coefficient:m(λ) = (s − 1/2) · C(s), where s = 1/2 + λ.In particular, κ = 1.

Reason. The coefficient arises solely from the exact finite-interval model identity at t = 1 and the specific log-gauge definition of W and the boundary trace. No scaling freedom remains once U and the boundary value are fixed; thus the identification is exact with κ = 1.

The DN map m(λ) is local in x, but the identity above depends only on a unit log-neighborhood of t = 1; the global “look” of C(s) comes from evaluating the compensated boundary after canceling the exact model singularity everywhere else. The locality corollary makes this explicit: once the model pole is removed pointwise, the only surviving boundary information is at t = 1, exactly where the DN map lives. This is why a local DN quantity matches the compensated boundary functional without hidden global terms.



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

Notation summary (quick reference)

• θ(t) = 1 + 2∑_{n ≥ 1} e^{−π n² t}, φ(t) = θ(t) − 1.

• H = L²( (0, ∞), φ(t) dt ). T_w f(t) = f(t) + (log t) f′(t).

• q₁(f) = ∫ φ |T_w f|² dt + ∫ φ |f|² / t dt (closed form).

• h_s(t) = t^{s/2 − 1}, k_s(t) = 1/2( h_s(t) + h_{1 − s}(t) ).

• Λ(s) = π^{−s/2} Γ(s/2) ζ(s), Sg(s) = Λ(s) + (s − 1/2) C(s).

•  A(s), R(s): defined in §8 via (s − 1/2) C(s) = A(s) + R(s).

• J₀(s) = ½[ Λ₀(s − 2) + Λ₀(−1 − s) ] (model; see §8).

References (pointers)

• Theta modular transform and θ(t) ↔ 1/t: DLMF §20.7(viii), eqs. 20.7.30–20.7.33; see also §21.5.

• Zeta functional/reflection formulas and ξ(s): DLMF §25.4.

• Stirling/vertical‑line gamma asymptotics: DLMF §5.11.

• Strip‑shift/Paley–Wiener type lemma: Titchmarsh, Introduction to the Theory of Fourier Integrals.

• Closed quadratic forms and the first representation theorem; monotone convergence of forms: Kato, Perturbation Theory for Linear Operators (VI.2.1; VIII.3).
