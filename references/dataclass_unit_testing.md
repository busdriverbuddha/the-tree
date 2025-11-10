Here’s a crisp, practical way to think about unit-testing Python dataclasses—focusing on *principles* and *what* to test rather than code.

# What a dataclass promises (so test those promises)

1. **Construction semantics**

   * Required vs. defaulted fields behave as declared.
   * `default_factory` creates *fresh* instances (no shared mutable state).
   * `init=False`/computed fields aren’t settable via `__init__` but are present after construction.
   * `__post_init__` runs and enforces any invariants or normalizations.

2. **Representation & introspection**

   * `__repr__`/`repr=False` choices expose (or hide) only intended fields.
   * Field order and names match your public contract (esp. if other code relies on them).
   * `slots=True` classes disallow unexpected attribute injection.

3. **Value invariants (your domain rules)**

   * Cross-field constraints hold (e.g., “start ≤ end”, “currency matches amount”).
   * Normalization is correct and idempotent (e.g., trimming, lowercasing).
   * Illegal states are rejected with clear, specific failures.

4. **Equality & hashing contract**

   * If `eq=True`, instances with equal field values compare equal; unequal ones don’t.
   * If `order=True`, ordering is consistent (antisymmetry, transitivity, totality as intended).
   * If `frozen=True` or `unsafe_hash=True`, hashing aligns with equality; *never* assert specific hash numbers—assert set/dict behavior instead.
   * Fields with `compare=False` are excluded from equality/ordering as intended.

5. **Immutability / mutability**

   * `frozen=True` actually prevents mutation (including via descriptors/properties).
   * Mutable fields behave intentionally (no shared defaults, copies where required).
   * `dataclasses.replace` yields a new object with the requested deltas, leaving the original untouched.

6. **Serialization shape (if the dataclass is a boundary object)**

   * `asdict`/`astuple` produce the expected *shape* (note: they deep-copy by default).
   * JSON (or other) representation is stable and backward-compatible if external systems rely on it.
   * Round-trip semantics (serialize → deserialize) preserve meaning, especially for enums, datetimes, decimals.

7. **Pattern matching & constructor ergonomics**

   * `__match_args__` (based on init field order) supports intended structural matching.
   * Positional vs. keyword initialization is as you expect (esp. if positional use is allowed).
   * Optional/Union fields: `None` means “absent” only where designed to.

8. **Performance/footprint expectations (only if material)**

   * “Cheap” value objects: creation, equality, and copying are within acceptable bounds for hot paths.
   * `slots=True` reduces attribute dictionary overhead where you depend on it.

9. **Interoperability with collaborators**

   * If the dataclass is used by ORMs/serializers/validators (e.g., marshmallow, pydantic bridges, FastAPI), confirm field names/types/metadata remain compatible.
   * Versioning/migrations: additions are backward-compatible; removals or renames fail loudly in dependent code.

# How deep to test (scope & boundaries)

* **Unit level:** Treat a dataclass like a *value object*. Test invariants, equality/hash/order, immutability, and representation in isolation.
* **Integration level:** If the dataclass is a *message* between layers, test the schema/contract at those boundaries (e.g., JSON shape, DB mapping), not the business logic again.
* **Don’t overfit to implementation:** Validate *behavioral contracts*, not private field arrangements or incidental algorithmic steps.

# Techniques that pay off

* **Property-based tests for invariants:** Generate legal/illegal combinations to exercise cross-field rules, equality properties, and ordering laws.
* **Boundary & edge cases:** Empty strings, zero/negative values, `None`, extreme lengths, NaN/inf (if floats), timezone-aware datetimes, large enums.
* **Mutation traps:** Explicitly test that mutable defaults aren’t shared; verify deep vs. shallow semantics where relevant (`asdict` deep-copy behavior, nested dataclasses).
* **Contract snapshots where appropriate:** Snapshot only *public shapes* (repr format, serialized keys), not ephemeral details like memory addresses or dict ordering unless guaranteed.

# Anti-patterns to avoid

* **Testing Python or dataclasses itself.** Don’t re-prove the standard library; test your *choices* (e.g., that a field is excluded from comparisons because you set `compare=False`).
* **Asserting exact hash integers or relying on object IDs.** Assert set/dict behavior and equality, not implementation specifics.
* **Over-specifying repr formatting** when it’s not a public contract (keep it flexible unless tools or logs depend on it).
* **Conflating unit tests with persistence or transport tests.** Keep serialization/ORM tests separate from core value-semantics tests.
