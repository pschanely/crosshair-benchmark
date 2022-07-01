# CrossHair Benchmarks

Benchmarking data and scripts to evaluate the performance of
[CrossHair](https://github.com/pschanely/CrossHair).

## Background

CrossHair finds counter-examples on a best-effort basis.
Sometimes it'll find a counterexample immediately, sometimes in hours, and sometimes
effectively never.

This repo aims to provide a realistic set of examples to help CrossHair understand
whether any given change privdes more benefit than harm.

## Contributions

Contributions are **strongly** encouraged - the postive impact of this benchmark suite
is driven by having plentiful, diverse, and realistic examples.

By contributing examples, you will help guide CrossHair performance, to the
benefit of yourself and others.

To contribute, just add one or more python files under a new, dated directory.
Each file should have one faulty contract, and CrossHair should be able to find a
counterexample for that contract. Please try to keep examples minimal, and remove
correct postconditions, so that we don't spend time analyzing those.

If you can scale the difficulty of your example, try to make it so that CrossHair
detects a problem in the 5 second - 5 minute range. (this strikes a balance between
running benchmarks in a reasonable amount of time and having meaningful headroom for
gains)

If you have an example where CrossHair does not find a counterexample at all, it's
better to submit
[an issue](https://github.com/pschanely/CrossHair/issues/new?assignees=&labels=missed%20bug&template=bug_report.md&title=)
than to create it as a benchmark example.
