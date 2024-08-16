# A Buck2–NativeLink Case Study

## Problem

This repo demonstrates an error I encountered while integrating NativeLink with Buck2 for remote execution. The problem is that NativeLink workers fail to locate executables (e.g., `rustc`) that are however locatable according to the `PATH` environment variable.

## Minimal Reproduction

- The `platforms` folder is adapted from Buck2 remote execution examples, modified to disable local execution.
- The root `BUCK` file contains a genrule target that runs `src/hello_nativelink.py`.
- `hello_nativelink.py` attempts to execute `rustc --version` and write the results to the output file.

## Error

Building the genrule target fails with the following error:

```console
root@439e9e6855a3:/workdir/buck2-nativelink-case-study# buck2 build //:hello_nativelink
Action failed: root//:hello_nativelink (genrule)
Remote command returned non-zero exit code 1
...
  File "/usr/lib/python3.12/subprocess.py", line 1955, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'rustc'
...
BUILD FAILED
Failed to build 'root//:hello_nativelink (prelude//platforms:default#904931f735703749)'
```

The build succeeds if `src/hello_nativelink.py` is modified to use the absolute path to `rustc`. This may suggest that the error relates to how a NativeLink worker handles the `PATH` environment variable.

## Questions

- Can I let NativeLink workers inherit the `PATH` environment variable?
- What are the best practices for resolving such "NotFound" issues?
