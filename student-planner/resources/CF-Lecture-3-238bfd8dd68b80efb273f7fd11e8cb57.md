
## CIA Triad


### Confidentiality

- A property that information is not disclosed to user, processes or device unless that have authorized to access the information
- Need to know basis for data access
- Implement using access control
- Verification of identity and authentication
- It is difficult to ensure and easiest to assess in terms of success ( binary in nature: Yes or No)

### Integrity

- A property whereby information, an information system or component of a system has not been modified or destroyed in an unauthorized manner
- It is:
	- Non binary (degrees of integrity)
	- Context dependent (means different things in different contexts)

### Integrity vs Confidentiality

- Integrity is concerned with the unauthorized modification of assets
- Confidentiality is concerned with access of the assets

### Availability

- A property of a system always being available during critical times

## CIANN

- CIA + Authentication & Authorization & Non-repudiation

## Need to balance CIA

- Example 1: C vs I+A
	- Disconnect computer from network to increase confidentiality
	- Availability suffers Integrity also suffer due to loss of updates
- Example 2: I VS C+A
	- Have extensive data checks by different people/systems to increase integrity
	- Confidentiality suffers as more people see data, availability suffers due to locks on data under verification

## Threat

- The threats is essentially the who or what that can do you harm if given an opportunity.
- They cannot do harm on they're own.

### Kind of threats:

1. Interception: An unauthorized party gains access
2. Interruption: Asset becomes unavailable
3. Modification: Unauthorized party changes state of asset
4. Fabrication: Unauthorized party counterfeits an asset

## Vulnerability


They are basically weakness that allows the threat to exploit you


![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/cb8bfd8d-d68b-81fa-ac15-000328a0aab4/fb9d5315-5a4c-4076-a155-42b872e47d87/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662O5ODQUF%2F20250815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250815T064757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLXdlc3QtMiJHMEUCIQCK%2BfmVWcFSm%2Bge%2BxiYf7qlDdsiGy21Gk47M1gFhP3vXAIgFEaeZiDlEFAD5pVBFEkLY1%2FQBSnq3U9ejGA2Rjv%2BvXQq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDAl%2BuRAicOFJyhMahircAzvhpzvspFDmRFyvVJ%2BEfErNE%2FHf3kSJJnhOgvkgHlHRmPJNJr%2BdKS3aAqzFWIA3vx48q6NWIhMIiUMEjtDcNqQ1ThOCb8DLpK4Qu%2FQgoJB04v%2BGm6aSjBTL5uR5eMdubNBFzD%2BTAXO3EoAT4DRxViq%2FtN1NXZaf520bjJ4u8qCumXGN05kHKekw1oG40ywduU3NMdP0ZTXvuguB8iYKUKFiy3SvQ%2BiazdPaSHgpWuXVNwv9ccFECGE0PO6%2FKSysT0cRqKnoO9qCFWz%2BhHnAMheba2KihMBCTcmamfpeDjZNHXgJ%2Bk%2BNA4KLXd4QsCTc3LLISSvg%2BJvxO0hjbP36ZhBWtsQq%2B7gEsy3B7tKka7Cl7JWN6vV1rCOG7uZvyC8EXRNjmmeiB42SNZnO5A%2F6cOytoIEqM4Rc%2F0PY8ezoseSl5dCGVc%2BlzUH7R3TtpxJruxdgom3LjI2n7Jta5%2BEItho%2BNQponkuq8Q8FGKI%2FlXyF7QdygWPthvODYW75mhmrD059EWXxv8YB1y0wRTkfyLj5ZDg4ntvOwfFSgp0Cuqkjgmo8WIZObY7jj37abbF14LBq6oE8oqxcGlGNF1SgK1%2Bm1G4TPh7YVXRKlK9gu3Sj%2FNOzdUkx4u1ByTzYMKKj%2B8QGOqUBNa%2Ft3M39B6LvUltTJ0fLfaPo34R%2B1YAZhOmTZSgjANB%2BDUrtoqZVDtevgxZLeYN73i%2Bdi9WFyqQ9uK7ci2Af6utLHVXVkyfZJd%2BYN66aJ%2F5wijsCPLaQW5ECfHEUm6drkDNjlw2hCae4C7lMUyQ81zyu4Zu3oPNUmFTrS3gjoAJ8Ju931d2anrB60QqLjfqeLQ28NDQaoAi%2FqejDjK1EswsqOccc&X-Amz-Signature=991d9e8797ece97f1556c346d86cfce55682d37b34f546dc81cbf26938749112&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


## Controls


Means and ways to block a threat, which tries to exploit one or more vulnerabilities


Example:- Cyclone Biparjoy


What were city vulnerabilities, threats and controls?


V- Geographical location near sea


T- Hurricane dam damage terrorist attack


C- Dams and other civil infrastructure


**DAD Triad (Goals of Malicious Attackers)**


**DAD** stands for the three primary objectives of attackers:

1. **Disclosure** – Unauthorized access or exposure of information

	_(Violates Confidentiality)_


	_e.g., leaking customer data_

2. **Alteration** – Unauthorized modification of data

	_(Violates Integrity)_


	_e.g., tampering with transaction records_

3. **Denial** – Disruption of access to systems or data

	_(Violates Availability)_


	_e.g., DDoS attack, ransomware locking systems_


**What Attackers Need: MOM**


To launch a successful attack, threat actors usually require:

1. **Motive** – The reason behind the attack
	- Financial gain
	- Political agenda
	- Revenge or curiosity
2. **Opportunity** – The chance to exploit a vulnerability
	- Weak passwords
	- Unpatched systems
	- Insider access
3. **Method** – The tools, techniques, and processes used
	- Phishing, malware, brute-force, social engineering

> 💡 Two-mark test @ [forms.cloud.microsoft/r/3V0b1t8RMd](https://forms.cloud.microsoft/r/3V0b1t8RMd)


![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/cb8bfd8d-d68b-81fa-ac15-000328a0aab4/0bd759f7-84b3-4006-bbaf-9076fd62b358/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662O5ODQUF%2F20250815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250815T064757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLXdlc3QtMiJHMEUCIQCK%2BfmVWcFSm%2Bge%2BxiYf7qlDdsiGy21Gk47M1gFhP3vXAIgFEaeZiDlEFAD5pVBFEkLY1%2FQBSnq3U9ejGA2Rjv%2BvXQq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDAl%2BuRAicOFJyhMahircAzvhpzvspFDmRFyvVJ%2BEfErNE%2FHf3kSJJnhOgvkgHlHRmPJNJr%2BdKS3aAqzFWIA3vx48q6NWIhMIiUMEjtDcNqQ1ThOCb8DLpK4Qu%2FQgoJB04v%2BGm6aSjBTL5uR5eMdubNBFzD%2BTAXO3EoAT4DRxViq%2FtN1NXZaf520bjJ4u8qCumXGN05kHKekw1oG40ywduU3NMdP0ZTXvuguB8iYKUKFiy3SvQ%2BiazdPaSHgpWuXVNwv9ccFECGE0PO6%2FKSysT0cRqKnoO9qCFWz%2BhHnAMheba2KihMBCTcmamfpeDjZNHXgJ%2Bk%2BNA4KLXd4QsCTc3LLISSvg%2BJvxO0hjbP36ZhBWtsQq%2B7gEsy3B7tKka7Cl7JWN6vV1rCOG7uZvyC8EXRNjmmeiB42SNZnO5A%2F6cOytoIEqM4Rc%2F0PY8ezoseSl5dCGVc%2BlzUH7R3TtpxJruxdgom3LjI2n7Jta5%2BEItho%2BNQponkuq8Q8FGKI%2FlXyF7QdygWPthvODYW75mhmrD059EWXxv8YB1y0wRTkfyLj5ZDg4ntvOwfFSgp0Cuqkjgmo8WIZObY7jj37abbF14LBq6oE8oqxcGlGNF1SgK1%2Bm1G4TPh7YVXRKlK9gu3Sj%2FNOzdUkx4u1ByTzYMKKj%2B8QGOqUBNa%2Ft3M39B6LvUltTJ0fLfaPo34R%2B1YAZhOmTZSgjANB%2BDUrtoqZVDtevgxZLeYN73i%2Bdi9WFyqQ9uK7ci2Af6utLHVXVkyfZJd%2BYN66aJ%2F5wijsCPLaQW5ECfHEUm6drkDNjlw2hCae4C7lMUyQ81zyu4Zu3oPNUmFTrS3gjoAJ8Ju931d2anrB60QqLjfqeLQ28NDQaoAi%2FqejDjK1EswsqOccc&X-Amz-Signature=25c132d2321855830d008bd2b59d3ad188eca68f1da2673b598ae48e043f8459&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

