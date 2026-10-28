# Target V2 app interface design

Status: architecture resources only. The preserved `screens/`, baseline guides and implementation handover remain historical source material; no target component/YAML implementation is delivered by this note.

Use [APP-COMPONENT-CONTRACTS.md](../../Others/architecture/APP-COMPONENT-CONTRACTS.md) for logical shared component inputs/events, workspace draft ownership, scope switches, validation and recovery display. Use the [screen map](../../Others/architecture/SCREEN-IMPLEMENTATION-MAP.md) to locate feature responsibilities and [operation interfaces](../../Others/architecture/interfaces/README.md) for draft request/result shapes.

Future per-screen/component resources will map these logical interfaces to actual supported Canvas controls/properties and Power Fx, with exact data/flow bindings, manual steps, expected evidence and rollback. These documents are not instructions to paste property names into Studio. Connector/access dependencies are in [the solution architecture](../../Others/architecture/SOLUTION-AND-CONNECTOR-ARCHITECTURE.md); the owner handles configuration with each feature under D072.

Keep the accepted visual style and guided forms. Selected-assets workspaces support per-asset changes; assigned stock responses never mutate master records; reconciliation application precedes final sign-off. No general setup prompt or company action is requested by publishing this design.

## First manual implementation resources

[Reference catalogue package](target-v2/reference-catalogues/README.md) now supplies exact control/property tables and formula-bar files for a read-only catalogue screen. This is a manual resource delivery, not compiled YAML or a deployed app. The original baseline resources remain unchanged.
