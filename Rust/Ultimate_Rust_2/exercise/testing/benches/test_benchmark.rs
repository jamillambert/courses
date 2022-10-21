use criterion::{black_box, criterion_group, criterion_main, Criterion};
use testing::{fizz_buzz};

pub fn test_benchmark(c: &mut Criterion) {
    // c.bench_function("sploosh", |b| {
    //     b.iter(|| sploosh(black_box(3), black_box(5), black_box(100)))
    // });
    c.bench_function("fizz_buzz", |b| {
        b.iter(|| fizz_buzz(black_box(3), black_box(5), black_box(100)))
    });
}

criterion_group!(benches, test_benchmark);
criterion_main!(benches);
