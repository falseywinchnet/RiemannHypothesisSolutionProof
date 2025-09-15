import Lake
open Lake DSL

package riemann_hypothesis

require mathlib from git "https://github.com/leanprover-community/mathlib4" @ "master"

@[default_target]
lean_lib Thesis {
  srcDir := "lean"
}
