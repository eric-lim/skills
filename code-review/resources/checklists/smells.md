# Code Smell Checklist

This checklist shows the code smells from Martin Fowler's book *Refactoring* that the **Style Subagent** evaluates when reviewing code changes.

> [!NOTE]
> Martin Fowler defines 24 code smells. This checklist only includes 12 because the omitted smells are either caught automatically by standard linters (e.g., long parameters) or require analyzing the entire codebase rather than just a local git diff hunk (e.g., large classes).

* **Mysterious Name**
  * *Description*: A function, variable, parameter, class, or module whose name is vague or fails to reveal its purpose.
  * *Refactoring Action*: 
    * **For functions, classes, or modules:** Rename the entity to clearly state its responsibility. If a concise name cannot be found, the entity may have too many responsibilities; consider extracting or splitting the code first.
    * **For variables or parameters:** Rename to clearly reflect the data it holds or its usage context.


* **Duplicated Code**
  * *Description*: The exact same code structure or similar logic shape appears in more than one place within the changed hunks or surrounding context.
  * *Refactoring Action*: Extract the shared code into a helper function, method, or utility class, and call it from both locations.

* **Feature Envy**
  * *Description*: A method or function that accesses data or calls methods of another class/object more frequently than its own.
  * *Refactoring Action*: Move the function or its parts into the class containing the data it is envious of.

* **Primitive Obsession**
  * *Description*: Using primitive types (e.g. strings, integers, lists) to represent domain concepts that carry logic or constraints (e.g., telephone numbers, emails, IP addresses, money).
  * *Refactoring Action*: Encapsulate the primitive in a small custom class, type, or schema constraint (Value Object pattern).

* **Shotgun Surgery**
  * *Description*: A single logical change forces multiple small modifications scattered across several different files or classes.
  * *Refactoring Action*: Move the scattered methods or fields (using *Move Method* or *Move Field*) to consolidate the related logic into a single class or module.

* **Speculative Generality**
  * *Description*: Hooks, excessive parameters, class structures, or generalization patterns created to support future "what ifs" that are not currently requested by the specification.
  * *Refactoring Action*: Delete the speculative code; inline back to the simplest working version.

* **Data Clumps**
  * *Description*: The same small group of fields or parameters travel together in multiple functions, classes, or method arguments.
  * *Refactoring Action*: Bundle them into a single custom class or Value Object, and pass that object instead.

* **Repeated Switches**
  * *Description*: The same conditional `switch` or `if/else` checks on type codes or categories are duplicated in multiple spots across the codebase.
  * *Refactoring Action*: Use *Replace Conditional with Polymorphism* (subclassing/interfaces) or extract the logic into a factory/lookup registry.

* **Divergent Change**
  * *Description*: One single file, module, or class is modified frequently for multiple, completely unrelated reasons.
  * *Refactoring Action*: Split the module into separate classes so that each has a single responsibility (Single Responsibility Principle) and changes for only one reason.

* **Message Chains**
  * *Description*: Long chains of object navigation (e.g. `a.getB().getC().getD().doSomething()`), forcing the client to depend on the intermediate relationships.
  * *Refactoring Action*: Hide the delegation path. Implement a wrapper method on B or C so the client calls B directly (Law of Demeter).

* **Middle Man**
  * *Description*: A class or function does nothing but delegate calls directly to another object or method without adding any value.
  * *Refactoring Action*: Remove the middle man class entirely and let the caller call the target directly.

* **Refused Bequest**
  * *Description*: A subclass inherits methods and data from a superclass but overrides or rejects most of the inherited behavior (violating Liskov Substitution Principle).
  * *Refactoring Action*: Replace inheritance with composition (create a field for the former superclass, delegate only what is needed).
