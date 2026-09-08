# Provider and machine independence

English | [简体中文](provider-machine-independence.zh-CN.md)

Provider neutrality does not mean pretending all providers behave identically. It means provider capabilities, lifecycle details, and evidence are admitted through explicit contracts rather than being hardwired into the definition of a Goal.

Machine independence follows the same rule. A machine can be an execution location or resource boundary, but it is not the durable identity of the development program. Migration and recovery must preserve authority and exact identity while refusing ambiguous external state.
