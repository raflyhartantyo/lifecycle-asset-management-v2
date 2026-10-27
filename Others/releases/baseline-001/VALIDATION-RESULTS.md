# baseline-001 — local validation results

Prepared 2026-10-27.

- PASS: exactly three main folders: Power Apps, Power Automate, Others.
- PASS: 88 source files (87 original archive files plus confirmed-decisions.md) match recorded SHA-256 hashes.
- PASS: one app with 30 YAML sources and matching per-file guides.
- PASS: supplied YAML validator parses all 30 files and resolves its checked references across 2,354 controls.
- PASS: 15 flow folders each include original definition, trigger contract, configuration worksheet, full action map, implementation guide, Claude handover and validation guidance.
- PASS: all 403 nested flow actions appear in the action maps; generated trigger contracts match source triggers.
- PASS: all JSON files parse and local Markdown links resolve.
- PASS: portable Graphify map has 952 nodes and 1,634 relationships; all node source paths resolve inside the repository.
- NOT RUN: Power Apps Studio/App Checker, flow execution, target-environment connection and permission checks, runtime import and end-to-end scenarios.
- PASS: private target repository and write access verified for raflyhartantyo/lifecycle-asset-management-v2.
- GitHub publication and remote file integrity are verified separately after upload.

Reproduce the static checks with validate_delivery.py and check_yaml.py using the commands in the root README. Company Claude returns runtime results using the handover template.
